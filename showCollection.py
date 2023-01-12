from dotenv import load_dotenv
import os
import pymongo
from itertools import islice
import pandas as pd

load_dotenv()

usr = os.getenv("USR")
password = os.getenv("PASS")

client = pymongo.MongoClient(f'mongodb+srv://{usr}:{password}@project.fq5sh6t.mongodb.net/?retryWrites=true&w=majority', connect=False)
db = client["reviews"]

print("connection success")

Collection = db["VinylAndCD"]

myquery = { "reviewerID": "A171I27YBM4FL6" }

doc = Collection.find_one(myquery)

df = pd.DataFrame.from_dict(doc, orient="index")

print(df)
