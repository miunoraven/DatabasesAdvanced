import time, redis
import pymongo as mongo

while True:
    r = redis.Redis(host='localhost', port=6379, db=0)

    client = mongo.MongoClient("mongodb ://127.0.0.1:27017")

    bitcoins_db = client["bitcoins"]
    topten = bitcoins_db["bitcoins_topten"]

    for key in client.scan_iter():
        hash = {    "Hash": client.hmget(key, "hash"),
                    "Time": client.hmget(key, "time"),
                    "USD": client.hmget(key, "usd"),
                    "BTC": client.hmget(key, "btc")
        }
        x = topten.insert_one(hash)
        r.delete(key)
    
    time.sleep(60)

