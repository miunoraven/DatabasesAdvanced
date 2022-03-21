import time, redis
import pymongo as mongo

while True:
    r = redis.Redis(host='localhost', port=6379, db=0)

    price = list()
    for key in client.scan_iter():
        price.append(client.hmget(key, "USD"))
    print(price)


    client = mongo.MongoClient("mongodb ://127.0.0.1:27017")

    bitcoins_db = client["bitcoins"]
    topten = bitcoins_db["bitcoins_topten"]
    
    # x = topten.insert_one(bitcoin)
    
    time.sleep(60)

