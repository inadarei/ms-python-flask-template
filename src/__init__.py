# coding=utf-8

"""
    src.module
    ~~~~~~~~~~~~~~

    Main source of the microservice.

    :copyright: (c) 2020 by Irakli Nadareishvili.
    :license: MIT, see LICENSE for more details.
"""

import logging

# logFormatter = '%(asctime)s %(levelname)s \
# [%(filename)s %(funcName)s():%(lineno)d] - %(message)s'

LOG_FORMATTER = '%(asctime)s %(levelname)s \
[%(module)s %(funcName)s():%(lineno)d] - %(message)s'

DATE_FORMAT = '%H:%M:%S'

logging.basicConfig(format=LOG_FORMATTER, datefmt=DATE_FORMAT,
                    level=logging.INFO)
