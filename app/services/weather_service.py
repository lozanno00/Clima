import requests

class WeatherService:
    API_URL = 'https://api.openweathermap.org/data/2.5/weather'
    API_KEY = 'TU_API_KEY_AQUI'

    def get_weather(self, region: str) -> dict:
        try:
            response = requests.get(f"{self.API_URL}?q={region}&appid={self.API_KEY}&units=metric")
            response.raise_for_status()
            data = response.json()
            return {
                'region': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'rainChance': data['clouds']['all']
            }
        except requests.RequestException as e:
            print(f"Error al obtener el clima: {e}")
            return {}
