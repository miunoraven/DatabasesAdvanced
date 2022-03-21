import time, redis
import pymongo as mongo

while True:
    r = redis.Redis(host='localhost', port=6379, db=0)

    client = mongo.MongoClient("mongodb://localhost:27017")

    bitcoins_db = client["bitcoins"]
    topten = bitcoins_db["bitcoins_topten"]

    for key in r.scan_iter():
        hash = {    "Hash": r.hmget(key, "hash")[0],
                    "Time": r.hmget(key, "time")[0],
                    "USD": r.hmget(key, "usd")[0],
                    "BTC": r.hmget(key, "btc")[0]
        }
        x = topten.insert_one(hash)
        r.delete(key)
    
    time.sleep(60)

