from pymongo import MongoClient
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context
# , ssl=True, ssl_cert_reqs=ssl.CERT_NONE

client = MongoClient("mongodb+srv://Test_Tae:12345@projecttae.mnikf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


db = client.todo_app

collection_name = db["todos_app"]
courses_collection = db["courses"]
