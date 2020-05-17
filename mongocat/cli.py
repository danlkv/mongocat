"""Console script for mongocat."""
import sys
import click

from mongocat import MongoCat

@click.group()
@click.option('--debug/--no-debug')
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()
@click.option('--username')
def greet(username):
    click.echo('Hello %s!' % username)


if __name__ == '__main__':
    cli(auto_envvar_prefix='GREETER')


@click.command()
@click.option('-R', '--read', is_flag=True)
@click.option('-W', '--write', is_flag=True)
@click.option('-p', '--parser', type=click.Choice(['json', 'yaml']), default='yaml')
@click.option('-u', '--url', help='MongoDB URI. format: mongodb://[username:password@]host1[:port1]...')
@click.option('-d', '--database')
@click.argument('collection')
def cli(read, write, **options):
    """Console script for mongocat."""
    conn = MongoCat(**options)

    if write:
        for line in sys.stdin:
           id = conn.writeln(line)
           print(id)

    if read:
        for obj in conn.iter_all():
            print(obj)

    return 0

def main():
    sys.exit(cli(auto_envvar_prefix='MONGOCAT'))  # pragma: no cover

if __name__ == "__main__":
    main()
