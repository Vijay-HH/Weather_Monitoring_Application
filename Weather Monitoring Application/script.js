document.addEventListener('DOMContentLoaded', () => {
    const fetchWeatherButton = document.getElementById('fetch-weather');
    const cityInput = document.getElementById('city-input');

    fetchWeatherButton.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent the default anchor behavior

        const city = cityInput.value;
        if (city) {
            // Make an AJAX call to fetch the weather summary
            fetch(`/summary?city=${encodeURIComponent(city)}`)
                .then(response => {
                    if (response.ok) {
                        return response.text();
                    } else {
                        throw new Error('Network response was not ok.');
                    }
                })
                .then(html => {
                    document.body.innerHTML = html; // Replace the body with the new summary HTML
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
        } else {
            alert('Please enter a city name.');
        }
    });
});
