import os
import sys
import logging as log
import redis

def env_var(name, default):
  return os.environ.get(name) if name in os.environ else default

redis_host = env_var("REDIS_HOST", '0.0.0.0')
redis_port = env_var("REDIS_PORT", '6379')
redis_db = env_var("REDIS_DB", '0')
redis_pwd = env_var("REDIS_PWD", '')

# this is a pointer to the module object instance itself.
this = sys.modules[__name__]
this.redis_conn = redis.Redis(host=redis_host, port=redis_port, \
                              db=redis_db, password=redis_pwd)

def save_user(user, user_id):
  try: 
    bret = this.redis_conn.set(user_id, user)
  except redis.RedisError:
    response = {
      "completion" : {"status": "error"}
    }
    log.info("Error while saving in Redis", exc_info=True)
  else: 
    response = {
      "completion": {
          "status": "success",
          "user_id" : user_id
      }
    }

  return response