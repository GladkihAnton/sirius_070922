import logging.config

import yaml


with open('config/logging.conf.yml', 'r') as f:
    LOGGING_CONFIG = yaml.full_load(f)


logging.config.dictConfig(LOGGING_CONFIG)


class ConsoleFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:

        return '[%s] %s' % ('test', super().format(record))


logger = logging.getLogger('tinder_bot')
