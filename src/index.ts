import { WeatherService } from './services/weatherService';
import { WeatherCard } from './components/WeatherCard';

function main() {
    const region = prompt('Introduce la región de España:') || '';
    const weatherService = new WeatherService();

    weatherService.getWeather(region).then((data) => {
        const weatherCard = new WeatherCard(data);
        weatherCard.render();
    }).catch((error) => {
        console.error('Error al obtener el clima:', error);
    });
}

main();
