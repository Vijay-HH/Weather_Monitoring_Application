Installation and Setup Instructions

Prerequisites

Before running this application, ensure you have the following installed:

Python 3.8+
Flask
Docker (optional, for containerization)
OpenWeatherMap API Key (you can sign up for free at OpenWeatherMap)
Step-by-Step Setup
Clone the Repository


git clone https://github.com/yourusername/weather-monitoring-app.git
cd weather-monitoring-app
Create a Virtual Environment If you're using PyCharm, you can use the built-in feature to create a virtual environment. Otherwise, run:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies Install the required Python packages:


pip install -r requirements.txt
Set Up Environment Variables Create a .env file in the root directory of your project and add your OpenWeatherMap API key:

makefile

API_KEY=your_openweather_api_key
Run the Flask Application Start the Flask development server:

flask run
By default, Flask will run the app on http://127.0.0.1:5000/.

Access the Application Open your browser and go to http://127.0.0.1:5000/. You should see the home page where you can enter a city name and retrieve weather data.

Running the Application in Docker
Build Docker Image

docker build -t weather-monitoring-app .
Run Docker Container

docker run -d -p 5000:5000 weather-monitoring-app
Access the Application Visit http://localhost:5000/ in your browser to access the application.