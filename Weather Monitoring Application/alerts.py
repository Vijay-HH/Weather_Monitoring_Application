def check_alerts(weather_data):
    alerts = []
    for data in weather_data:
        if data['temp'] > 35:
            alerts.append(f"High temperature alert for {data['city']}!")
    return alerts
