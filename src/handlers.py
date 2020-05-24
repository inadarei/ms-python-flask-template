import logging as log
import uuid
import json

from . import model

def greeter(name):
  return f"Hello {name}!"

def save_user(user, user_id = ""):
  if (user_id == ""): 
    user_id = str(uuid.uuid4())
  log.info("Saving USER_ID: " + user_id)
  
  user = json.dumps(user)

  return model.save_user(user, user_id)
