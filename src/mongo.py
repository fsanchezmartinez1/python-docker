from pymongo import MongoClient
client = MongoClient()
client = MongoClient(host="172.20.0.6", port=27017,username="root",password="example")
db = client.users
users = db.user
user = {"name":"Fer","surname":"Sanchez"}
result = users.insert_one(user)