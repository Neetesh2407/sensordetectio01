from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://Neetesh:12345@cluster0.oibqarz.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

DATABASE_NAME = "PWskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("/content/wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis = 1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)