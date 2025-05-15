"""Basic connection example.
"""
import datetime
import json

import redis

r = redis.Redis(
    host='redis-13230.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=13230,
    decode_responses=True,
    username="default",
    password="fihy5nfmIrUXw8gOwJcLYcOHSjPYuwIq",
)

# r.set('myAutho', 'BMW M5 F90')
# r.set('myPet', 'Cat', ex=7200)
# r.lpush('list of products', 'milk', 'meat', 'egg', 'ice cream', 'onion')
# r.expire('list of products', 604800)
# r.lpush("tort recept", "flour:250")
# r.lpush("tort recept", "milk:500")
# r.lpush("tort recept", "sugar:300")
# r.lpush("tort recept", json.dumps({'sugar': 300}))
# r.delete('sugar:300')
# r.lpush("tort recept", 'sugar:500')
# r.delete('tort recept')
