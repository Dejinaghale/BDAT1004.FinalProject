# Import necessary modules
from flask import Flask
from api.data_transformer import data_transformer_app
from visualization.chart_generator import visualization_app
from database.mongodb_connector import get_mongo_collection
from app_config import config

# Create a Flask application
app = Flask(__name__)

# Load configurations from the Config class
app.config.from_object(config)

# Connect to MongoDB and set the collection attribute on the app config
app.config['collection'] = get_mongo_collection(app.config['MONGODB_URI'])

# Register blueprints for data transformation and visualization
app.register_blueprint(data_transformer_app)
app.register_blueprint(visualization_app)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
