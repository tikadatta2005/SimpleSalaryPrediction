from pymongo import MongoClient as mongo

client = mongo("mongodb://127.0.0.1:27017")
db = client["simpleML"]

collection = db["salary"]