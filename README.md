# Crawler

Flask API

    This Flask API extracts pricing data from a website and provides endpoints to retrieve the data in JSON format.

Prerequisites

    Python 3.x installed on your system
    pip package manager

Installation

    1.   Clone this repo or download the source kod
         git clone https://github.com/Lazarr03/Crawler.git
    2.   Navigate to the project directory
         cd <project_directory>
    3.   Install the required dependencies using pip
         pip install Flask requests beautifulsoup4 pandas

Running the Flask API
    1.   Open a terminal or command prompt
    2.   Navigate to the project directory where app.py is located
    3.   Run the Flask application by executing the app.py file.
         python app.py
    4.   Once the server is running, you can access the API endpoints using the following URLs:

         To convert Excel data to JSON: http://127.0.0.1:5000/api/crawler (Send a POST request)
         To retrieve pricing data: http://127.0.0.1:5000/api/pricing_data (Send a GET request)

         You can add a query parameter product_name to filter pricing data based on product name:

         Example: http://127.0.0.1:5000/api/pricing_data?product_name=prukaloprid

         To stop the Flask server, press Ctrl + C in the terminal where the server is running.

Used Postman for testing

Recommend using Postman or similar services for sending POST and GET requests 