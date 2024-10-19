import matplotlib.pyplot as plt

def plot_weather_trends(data):
    cities = [d['city'] for d in data]
    temps = [d['avg_temp'] for d in data]

    plt.bar(cities, temps)
    plt.xlabel('Cities')
    plt.ylabel('Average Temperature (C)')
    plt.title('Daily Average Temperature by City')
    plt.show()
