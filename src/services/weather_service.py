import requests

class WeatherService:
    API_URL = 'https://api.openweathermap.org/data/2.5/weather'
    API_KEY = '5c03313718cde027d45986b4d7e33685'  # Reemplaza 'TU_API_KEY_AQUI' con tu clave de API válida

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
        except requests.HTTPError as e:
            if e.response.status_code == 401:
                print("Error: Clave de API inválida. Por favor, verifica tu configuración.")
            else:
                print(f"Error HTTP al obtener el clima: {e}")
            return {}
        except Exception as e:
            print(f"Error inesperado al obtener el clima: {e}")
            return {}
