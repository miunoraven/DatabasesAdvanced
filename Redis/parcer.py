import time, redis
import pymongo as mongo

while True:
    r = redis.Redis(host='localhost', port=6379, db=0)

    client = mongo.MongoClient("mongodb ://127.0.0.1:27017")

    bitcoins_db = client["bitcoins"]
    topten = bitcoins_db["bitcoins_topten"]
    
    for items in transactions:
        bitcoin = { "hash": items[3], 
                    "time": items[1], 
                    "usd": items[0], 
                    "btc": items[2]
                    }
        r.hset(items[3], mapping=bitcoin)
    
    time.sleep(60)

