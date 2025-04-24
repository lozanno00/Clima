export class WeatherCard {
    private region: string;
    private temperature: number;
    private humidity: number;
    private rainChance: number;

    constructor(data: { region: string; temperature: number; humidity: number; rainChance: number }) {
        this.region = data.region;
        this.temperature = data.temperature;
        this.humidity = data.humidity;
        this.rainChance = data.rainChance;
    }

    render() {
        console.log(`Clima en ${this.region}:`);
        console.log(`- Temperatura: ${this.temperature}°C`);
        console.log(`- Humedad: ${this.humidity}%`);
        console.log(`- Probabilidad de lluvia: ${this.rainChance}%`);
    }
}
