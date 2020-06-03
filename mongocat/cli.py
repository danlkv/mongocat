"""Console script for mongocat."""
import sys
import click
import json
from bson import json_util

from mongocat import MongoCat


@click.command()
@click.option('-R', '--read', is_flag=True)
@click.option('-W', '--write', is_flag=True)
@click.option('-F', '--find', is_flag=True)
@click.option('-q', '--query', help='Query for find' )
@click.option('-p', '--parser', type=click.Choice(['json', 'yaml', 'bson']),
              default='yaml')
@click.option('-u', '--url',
              help=('MongoDB URI.'
                    'format: mongodb://[username:password@]host1[:port1]...')
              )
@click.option('-d', '--database', help='Database name')
@click.option('-f', '--update_on_exists', default=True, is_flag=True)
@click.argument('collection')
def cli(read, write, find, **options):
    """Read/write to mongodb COLLECTION."""
    conn = MongoCat(**options)

    if write:
        for line in sys.stdin:
            id = conn.writeln(line)
            if id is None:
                print(f'E: Nothing inserted for `{line}`', file=sys.stderr)
            else:
                print(id)

    def print_(obj):
        print(json_util.dumps(obj))#, default=json_util.default))

    if read:
        for obj in conn.iter_all():
            print_(obj)

    if find:
        query = json.loads(options['query'])
        for obj in conn.iter_query(query):
            print_(obj)

    return 0


def main():
    sys.exit(cli(auto_envvar_prefix='MONGOCAT'))  # pragma: no cover


if __name__ == "__main__":
    main()
