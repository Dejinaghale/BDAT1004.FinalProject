# Import necessary modules
from pymongo import MongoClient

# Define a function to retrieve MongoDB collection
def get_mongo_collection(mongo_uri):
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    
    # Access the database and collection
    database = client["chicago_crime_db"]
    collection = database['chicago_crime_collection']
    
    # Return the collection
    return collection
