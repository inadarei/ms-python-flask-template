""" Model implementation - saves data to the database """
import os
import sys
import logging as log
import redis

def env_var(name, default):
    """Safely retrieve an env var, with a default"""
    return os.environ.get(name) if name in os.environ else default

REDIS_HOST = env_var("REDIS_HOST", '0.0.0.0')
REDIS_PORT = env_var("REDIS_PORT", '6379')
REDIS_DB = env_var("REDIS_DB", '0')
REDIS_PWD = env_var("REDIS_PWD", '')

# this is a pointer to the module object instance itself.
# pylint: disable=invalid-name
this = sys.modules[__name__]
this.redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, \
                              db=REDIS_DB, password=REDIS_PWD)

def save_user(user, user_id):
    """Saves user into redis database"""
    try:
        this.redis_conn.set(user_id, user)
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
