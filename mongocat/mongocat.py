"""Main module."""

from pymongo import MongoClient
import yaml
import json


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
                 ):
        self.database_name = database
        self.collection_name = collection
        self.url = url
        self.parser = get_parser(parser)

        self.client = MongoClient(url)
        self.database = self.client[self.database_name]
        self.collection = self.database[self.collection_name]

    def writeln(self, line):
        object = self.parser(line)
        self.put(object)

    def put(self, object):
        id = self.collection.insert_one(object).inserted_id
        return id

    def iter_all(self):
        for obj in self.collection.find():
            yield obj
