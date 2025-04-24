import tkinter as tk
from tkinter import messagebox
from services.weather_service import WeatherService
from components.WeatherCard import WeatherCard

def get_weather():
    region = region_entry.get().strip()
    
    if not region:
        messagebox.showerror("Error", "No se ha introducido ninguna región.")
        return

    weather_service = WeatherService()
    
    try:
        data = weather_service.get_weather(region)
        if data:
            weather_card = WeatherCard(data)
            weather_card.render_to_window(result_label)
        else:
            messagebox.showinfo("Información", f"No se encontró información para la región: {region}.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener el clima: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación del Clima")

# Etiqueta y entrada para la región
tk.Label(root, text="Introduce la región de España:").pack(pady=5)
region_entry = tk.Entry(root, width=30)
region_entry.pack(pady=5)

# Botón para obtener el clima
tk.Button(root, text="Obtener Clima", command=get_weather).pack(pady=10)

# Etiqueta para mostrar los resultados
result_label = tk.Label(root, text="", justify="left", font=("Arial", 10))
result_label.pack(pady=10)

# Inicia la aplicación
root.mainloop()
