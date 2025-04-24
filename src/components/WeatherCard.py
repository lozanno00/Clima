class WeatherCard:
    def __init__(self, data: dict):
        self.region = data.get('region', '')
        self.temperature = data.get('temperature', 0)
        self.humidity = data.get('humidity', 0)
        self.rain_chance = data.get('rainChance', 0)

    def render_to_window(self, label):
        result_text = (
            f"Clima en {self.region}:\n"
            f"- Temperatura: {self.temperature}°C\n"
            f"- Humedad: {self.humidity}%\n"
            f"- Probabilidad de lluvia: {self.rain_chance}%"
        )
        label.config(text=result_text)
