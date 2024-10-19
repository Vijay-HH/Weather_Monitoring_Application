from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary', methods=['GET'])
def summary():
    # You would replace this with logic to retrieve actual weather data
    city = request.args.get('city', 'Default City')
    average_temp = 25  # Sample value
    dominant_condition = "Clear"  # Sample value
    max_temp = 30  # Sample value
    min_temp = 20  # Sample value
    last_updated = "2024-10-18 10:00 AM"  # Sample value
    alert_threshold = 35  # Sample value
    return render_template('summary.html', city=city, average_temp=average_temp,
                           dominant_condition=dominant_condition, max_temp=max_temp,
                           min_temp=min_temp, last_updated=last_updated,
                           alert_threshold=alert_threshold)

if __name__ == '__main__':
    app.run(debug=True)
