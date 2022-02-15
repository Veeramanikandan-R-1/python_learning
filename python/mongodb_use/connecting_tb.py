import pymongo

myclient = pymongo.MongoClient("mongodb+srv://mieupro:PrOMKTUIsMFFncR2@mieupro-cluster.hqvoj.mongodb.net/lavazza?retryWrites=true&w=majority")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
mydb=myclient.list_database_names()