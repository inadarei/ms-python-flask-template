import redis
r = redis.Redis(host="ms-redis", password="4n_ins3cure_P4ss")
r.set("ikuna", "grr")
print ("iko: " + str(r.get("ikuna")))
