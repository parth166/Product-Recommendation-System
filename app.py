from dotenv import load_dotenv
import os

load_dotenv()

usr = os.getenv("USR")
password = os.getenv("PASS")
path=os.getenv("LocalPath")

import pymongo
from pymongo import MongoClient
client = pymongo.MongoClient(f'mongodb+srv://{usr}:{password}@project.fq5sh6t.mongodb.net/?retryWrites=true&w=majority')
print("connection successful!")
client.close()

