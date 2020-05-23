"""Main module."""

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import yaml
import json
import sys


def get_parser(parser_name):
    if parser_name == 'yaml':
        return yaml.safe_load
    if parser_name == 'json':
        return json.loads


class MongoCat:
    def __init__(self,
                 database,
                 collection,
                 url,
                 parser='yaml'
                 ,update_on_exists=True
                 ):
        self.database_name = database
        self.collection_name = collection
        self.update_on_exists = update_on_exists
        self.url = url
        self.parser = get_parser(parser)

        self.client = MongoClient(url)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]

    def on_error(self, error):
        print(f'E: {error}', file=sys.stderr)

    def writeln(self, line):
        if len(line) > 1:
            object = self.parser(line)
            print(object)
            try:
                id = self.put(object, self.update_on_exists)
                return id
            except Exception as e:
                self.on_error(e)

    def put(self, object, update_on_exists=True):
        try:
            id = self.collection.insert_one(object).inserted_id
        except DuplicateKeyError:
            if update_on_exists:
                result = self.collection.replace_one(
                    {'_id': object['_id']}
                    ,object, upsert=True
                )
                id = object['_id']
            else:
                raise
        return id

    def iter_all(self):
        for obj in self.collection.find():
            yield obj
