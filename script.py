'''
    This is a file for random python scripts testing
'''

from dotenv import load_dotenv
import os
import json
import pymongo
from itertools import islice
import pandas as pd
import random

load_dotenv()

usr = os.getenv("USR")
password = os.getenv("PASS")

client = pymongo.MongoClient(f'mongodb+srv://{usr}:{password}@project.fq5sh6t.mongodb.net/?retryWrites=true&w=majority')
db = client["reviews"]

Collection = db["VinylAndCD"]

f = open("VinylAndCD.txt", "w")
for document in Collection.find():
    obj = {
        "_id":str(document["_id"]),
        "asin":str(document["asin"]),
        "reviewerID":document["reviewerID"],
        "reviewerName":document["reviewerName"],
        "overall":document["overall"],
        "verified":str(document["verified"])
    }
 
    stringToWrite = str(obj).replace(" ","")
    stringToWrite = stringToWrite.replace("\'","\"")
    f.write(stringToWrite+"\n")

db = client["metaData"]

Collection = db["VinylAndCD"]

f = open("metaVinylAndCD.txt", "w")
for document in Collection.find():
    buy = document["also_buy"]
    view = document["also_view"]

    similar = list(set(buy + view))
    random.shuffle(similar)

    count = 0
    for prod in similar:
        obj = {
            "_id":str(document["_id"]),
            "asin":str(document["asin"]),
            "similar":str(prod)
        }
        count+=1
        if count == 6:
            break

        stringToWrite = str(obj).replace(" ","")
        stringToWrite = stringToWrite.replace("\'","\"")
        f.write(stringToWrite+"\n")

myquery = { "$where": { "also_buy.length > 0 || also_view.length > 0" } }

count = 0

data = []

for document in Collection.find():
    if document["also_buy"] != None and len(document["also_buy"]) > 0:
        data.append(document)
    elif document["also_view"] != None and len(document["also_view"]) > 0:
        data.append(document)

# Collection.drop()
r = Collection.insert_many(data)
    
# count = DigitalMusic.count_documents(myquery)
print(count)

with open("data/CDs_and_Vinyl.json") as f:
    lines = list(islice(f, 1))
    for line in lines:
        obj = json.loads(line)
        df = pd.DataFrame.from_dict(obj, orient="index")
        print(df)