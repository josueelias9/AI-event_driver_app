import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe("publi")
while True:
    print(p.get_message())
    time.sleep(.1)