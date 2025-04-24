export class WeatherService {
    private API_URL = 'https://api.openweathermap.org/data/2.5/weather';
    private API_KEY = '5c03313718cde027d45986b4d7e33685';

    async getWeather(region: string): Promise<{ region: string; temperature: number; humidity: number; rainChance: number }> {
        const response = await fetch(`${this.API_URL}?q=${region}&appid=${this.API_KEY}&units=metric`);
        if (!response.ok) {
            throw new Error('No se pudo obtener el clima');
        }

        const data = await response.json();
        return {
            region: data.name,
            temperature: data.main.temp,
            humidity: data.main.humidity,
            rainChance: data.clouds.all
        };
    }
}
