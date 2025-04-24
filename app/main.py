from services.weather_service import WeatherService
from components.weather_card import WeatherCard

def main():
    region = input("Introduce la región de España: ")
    weather_service = WeatherService()
    data = weather_service.get_weather(region)

    if data:
        weather_card = WeatherCard(data)
        weather_card.render()
    else:
        print("No se pudo obtener el clima.")

if __name__ == "__main__":
    main()
