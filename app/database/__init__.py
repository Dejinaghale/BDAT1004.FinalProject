# Import necessary modules
from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Set the 'MONGODB_URI' configuration option
app.config['MONGODB_URI'] = 'mongodb://localhost:27017/mydatabase'

# Other configurations and code...

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
