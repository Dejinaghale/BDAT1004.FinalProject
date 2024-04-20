from pymongo import MongoClient

# Define a function to retrieve a MongoDB collection
def get_mongo_collection(mongo_uri):
    # Connect to the MongoDB server using the provided URI
    client = MongoClient(mongo_uri)
    # Access the "chicago_crime_db" database
    database = client["chicago_crime_db"]
    # Retrieve the "chicago_crime_collection" collection
    collection = database['chicago_crime_collection']
    # Return the collection
    return collection
