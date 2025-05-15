"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-13230.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=13230,
    decode_responses=True,
    username="default",
    password="fihy5nfmIrUXw8gOwJcLYcOHSjPYuwIq",
)


pubsub = r.pubsub()
pubsub.subscribe('school_channel')
for massage in pubsub.listen():
    print(massage)