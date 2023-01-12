from dotenv import load_dotenv
import os
import json
import pymongo
from itertools import islice

load_dotenv()

usr = os.getenv("USR")
password = os.getenv("PASS")
path=os.getenv("LOCAL")

client = pymongo.MongoClient(f'mongodb+srv://{usr}:{password}@project.fq5sh6t.mongodb.net/?retryWrites=true&w=majority')

db = client["metaData"]

filepaths = [f'{path}meta_CDs_and_Vinyl.json']

collectionNames = ["VinylAndCD"]

mapping = {}

for idx, collection in enumerate(collectionNames):
    mapping[collection] = filepaths[idx]

for collection, filepath in mapping.items():
    collection = db[collection]
    data = []

    with open(filepath) as f:
        lines = f.read().splitlines()
        for line in lines:
            obj = json.loads(line)
            if (len(obj['also_buy']) > 0 or len(obj['also_view']) > 0):
                temp = {
                    "asin": obj['asin'],
                    "also_buy": obj['also_buy'],
                    "also_view": obj['also_view']
                } 
                data.append(temp)
    
    r = collection.insert_many(data)

db2 = client["reviews"]

filepaths = [f'{path}CDs_and_Vinyl.json']

collectionNames = ["VinylAndCD"]

mapping = {}

for idx, collection in enumerate(collectionNames):
    mapping[collection] = filepaths[idx]

for collection, filepath in mapping.items():
    collection = db2[collection]
    data = []

    with open(filepath) as f:
        lines = list(islice(f, 300000))
        count = 1

        for line in lines:
            if count == 300000: 
                break

            obj = json.loads(line)

            also_buy = []
            also_view = []

            if obj.get("reviewerName") == None or obj.get("reviewerID") == None:
                continue

            temp = {
                "asin": obj['asin'],
                "reviewerID": obj['reviewerID'],
                "reviewerName": obj['reviewerName'],
                "overall": obj["overall"],
                "verified": obj["verified"]
            }

            count += 1

            data.append(temp)
    
    r = collection.insert_many(data)
