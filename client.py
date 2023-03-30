import redis
r = redis.Redis(decode_responses=True)
r.set('key','value')
print(r.get('shalom'))
