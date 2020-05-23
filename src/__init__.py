import logging

# logFormatter = '%(asctime)s %(levelname)s \
# [%(filename)s %(funcName)s():%(lineno)d] - %(message)s'

logFormatter = '%(asctime)s %(levelname)s \
[%(module)s %(funcName)s():%(lineno)d] - %(message)s'

dateformat = '%H:%M:%S'
#dateformat = '%Y-%m-%d:%H:%M:%S'
logging.basicConfig(format=logFormatter, datefmt=dateformat, \
  level=logging.INFO)