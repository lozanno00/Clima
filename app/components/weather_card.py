class WeatherCard:
    def __init__(self, data: dict):
        self.region = data.get('region', '')
        self.temperature = data.get('temperature', 0)
        self.humidity = data.get('humidity', 0)
        self.rain_chance = data.get('rainChance', 0)

    def render(self):
        print(f"Clima en {self.region}:")
        print(f"- Temperatura: {self.temperature}°C")
        print(f"- Humedad: {self.humidity}%")
        print(f"- Probabilidad de lluvia: {self.rain_chance}%")
