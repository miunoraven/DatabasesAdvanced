import requests, time, re
from bs4 import BeautifulSoup

result = list()
# keep going until manually stopped
while True:
    minutes = 0
    # print every 5 minutes
    while minutes < 5:
        transactions = list()
        respose = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
        bitcoin_data = BeautifulSoup(respose.text, features="html.parser")
        # USD, BTC and time falls all under the same class, so prices has all the information except the hash
        prices = bitcoin_data.findAll('span', attrs={"class" : "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})
        # get all the hashes in the same order
        hashes = bitcoin_data.findAll('a', attrs={"class" : "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})

        count = 0
        transaction = list()

        for price in prices:
            count += 1
            # remove all unneccesary words so it is easier to sort
            price = re.sub("\$", "", price.text)
            price = re.sub(" BTC", "", price)
            price = re.sub(",", "", price)
            # make a list of time, hash, usd and btc and add it to transactions list (make matrix)
            # if all elements (time, usd, btc) are added, add hashes and add to transactions list
            if count % 3 == 0:
                transaction.append(hashes[(count//3)-1].text)
                # make sure USD comes from to sort easier later
                transaction.insert(0,float(price))
                transactions.append(transaction)
                transaction = []
            # add to transaction to make a list for transactions
            else: 
                transaction.append(price)

        # sort on USD on descending
        transactions = sorted(transactions, reverse=True)

        # if top 10 list is empty, the first ten become the list
        if len(result) == 0:
            for i in range(0,10):
                result.append(transactions[i])

        # morf the two top 10 together to get the highest 10 transactions
        else:
            result += transactions[:10]
            result = sorted(result, reverse=True)[:10]
        
        # print a top 10 list every minute
        minutes +=1
        print("TOP 10 TRANSACTIONS:")
        for idx in range(0,len(result)):
            print(str(idx+1) + ": $" + str(result[idx][0]))

        # wait a minute
        time.sleep(60)

    # print a top 10 result after 5 minutes
    print("RESULT AFTER 5 MIN:")
    for idx in range(0,len(result)):
        print("Time: " + result[idx][1], "Hash: " + result[idx][3], "USD: $" + str(result[idx][0]), "BTC: " + result[idx][2])

