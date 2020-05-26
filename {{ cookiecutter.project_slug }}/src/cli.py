import click
import coloredlogs, logging

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')
coloredlogs.install(level='DEBUG', logger=logger)


@click.command()
@click.option("--count", default=1, help="Number of greetings")
@click.option("--name", prompt="Your Name", help="The person to greet")
def app(count, name):
    """Simple program to greet name for total COUNT times"""
    logger.debug("this is a debugging message")
    logger.info("this is an informational message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")
    logger.critical("this is a critical message")
    for _ in range(count):
        click.echo(f"Hello, {name}")

