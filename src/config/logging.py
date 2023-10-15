from sys import stdout

from loguru import logger

FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>\n"  # noqa


def formatter(record):
    name = record['name']
    module_tree = name.split('.')
    record['name'] = '.'.join(module[0] for module in module_tree)

    return FORMAT


def configure_logger():
    logger.remove()
    logger.add(stdout, format=formatter, level="DEBUG", colorize=False)
