import requests
import time
from database.mongodb_connector import get_mongo_collection
from script_config import Config

# Define a function to acquire and store data in MongoDB
def acquire_and_store_data():
    # Define the URL for the City of Chicago API
    chicago_api_url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
    
    # Send a GET request to the API endpoint
    response = requests.get(chicago_api_url)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Extract JSON data from the response
        data = response.json()
        
        # Retrieve the MongoDB collection using the provided URI
        collection = get_mongo_collection(Config.MONGODB_URI)
        
        # Insert the acquired data into the MongoDB collection
        collection.insert_many(data)
        
        # Print a success message
        print("Data acquired and stored successfully.")
    else:
        # Print an error message if the response is not successful
        print(f"Error: {response.status_code}")

# Run the acquisition process continuously
while True:
    acquire_and_store_data()  # Call the function to acquire and store data
    time.sleep(60*60*24)  # Wait for 24 hours before running the process again
