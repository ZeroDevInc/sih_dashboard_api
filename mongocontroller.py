import pymongo

def mongoconnector(collection_name):
    client = pymongo.MongoClient("mongodb+srv://mongo:mongo@cluster0.4cvm33l.mongodb.net/?retryWrites=true&w=majority")  # Replace with your MongoDB connection string
    db = client["sih"]  # Replace with your database name
    collection_obj = db[collection_name]
    return collection_obj
