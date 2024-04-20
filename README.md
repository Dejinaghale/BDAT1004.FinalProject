# Chicago Crime Dashboard

## Overview

The Flask-based web application functions as a dashboard for Chicago Crime, offering visual representations and 
analyses derived from crime data sourced from the City of Chicago. It retrieves information from the Chicago Crime API,
stores it within a MongoDB database, and presents it through Google Charts for visualization purposes.

## Project Hierarchy

```
BDAT1004.FINALPROJECT/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── data_transformer.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── chart_generator.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── mongodb_connector.py
│   ├── templates/
│       ├── dashboard.html
│   ├── app_config.py
├── scripts/
│   ├── import_data_script.py
    ├── script_config.py
├── requirements.txt
├── README.md
├── .gitignore
```

## Project Structure

- **`app/`**: This directory holds the core logic of the application.
  - **`main.py`**: Functions as the primary entry point for the Flask application.
  - **`api/`**: This module manages API-related tasks.
    - **`data_transformer.py`**: Serves as a blueprint for fetching necessary data.
  - **`visualization/`**: Responsible for handling data visualization tasks.
    - **`chart_generator.py`**: Functions as a blueprint for generating charts and rendering the dashboard.
  - **`database/`**: This module handles functionalities related to the database.
    - **`mongodb_connector.py`**: Contains utility functions for establishing connections to MongoDB.
  - **`templates/`**: Stores HTML templates, including `dashboard.html`.

- **`scripts/`**: This directory contains scripts relevant to the project.
  - **`data_import_script.py`**: Used for importing data from the Chicago Crime API at 24-hour intervals.

- **`config.py`**: Houses the configuration settings for the Flask application.

- **`requirements.txt`**: Lists all the Python dependencies required for the project.
- 
## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone 
   cd BDAT1004.FinalProject
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MongoDB:**

   - Create a MongoDB Atlas account or use a local MongoDB instance.
   - Update the MongoDB URI in `config.py`.

4. **Run the Application:**

   ```bash
   python3 app/main.py
   ```

   Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Running Data Import Script

To run the data import script, execute the following command:

```bash
python scripts/data_import_script.py
```

This script fetches data from the Chicago Crime API and stores it in the MongoDB database.

## Configuration

- **`config.py`**: Update the MongoDB URI and other configuration settings.

## Contributing

Contributions are welcome!

```
