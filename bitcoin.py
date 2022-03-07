import requests, time, re
from bs4 import BeautifulSoup

result = list()
while True:
    minutes = 0
    while minutes < 5:
        transactions = list()
        respose = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
        bitcoin_data = BeautifulSoup(respose.text, features="html.parser")
        prices = bitcoin_data.findAll('span', attrs={"class" : "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})
        hashes = bitcoin_data.findAll('a', attrs={"class" : "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})

        count = 0
        transaction = list()

        for price in prices:
            count += 1
            price = re.sub("\$", "", price.text)
            price = re.sub(" BTC", "", price)
            price = re.sub(",", "", price)
            if count % 3 == 0:
                transaction.append(hashes[(count//3)-1].text)
                transaction.insert(0,float(price))
                transactions.append(transaction)
                transaction = []
            else: 
                transaction.append(price)

        transactions = sorted(transactions, reverse=True)
        if len(result) == 0:
            for i in range(0,10):
                result.append(transactions[i])
        else:
            result += transactions[:10]
            result = sorted(result, reverse=True)[:10]
        
        minutes +=1
        print("TOP 10 TRANSACTIONS:")
        for idx in range(0,len(result)):
            print(str(idx+1) + ": $" + str(result[idx][0]))

        time.sleep(60)

    print("RESULT AFTER 5 MIN:")
    for idx in range(0,len(result)):
        print("Time: " + result[idx][1], "Hash: " + result[idx][3], "USD: $" + str(result[idx][0]), "BTC: " + result[idx][2])

