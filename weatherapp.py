import tkinter as tk
from tkinter import messagebox
import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_location(city):
    """Find the coordinates of a city."""
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(
        GEOCODING_URL,
        params=params,
        timeout=10
    )
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        raise ValueError("City not found.")

    return data["results"][0]


def get_weather(latitude, longitude):
    """Retrieve current weather for given coordinates."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "surface_pressure,"
            "wind_speed_10m,"
            "weather_code"
        ),
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh"
    }

    response = requests.get(
        WEATHER_URL,
        params=params,
        timeout=10
    )
    response.raise_for_status()

    return response.json()


def weather_description(code):
    """Convert Open-Meteo weather code into readable text."""
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }

    return descriptions.get(code, "Unknown conditions")


def display_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning(
            "Missing City",
            "Please enter a city name."
        )
        return

    try:
        location = get_location(city)

        weather = get_weather(
            location["latitude"],
            location["longitude"]
        )

        current = weather["current"]

        location_name = location["name"]

        if location.get("country"):
            location_name += f", {location['country']}"

        city_result.config(text=location_name)

        temperature_result.config(
            text=f"{current['temperature_2m']:.1f} °C"
        )

        feels_result.config(
            text=f"{current['apparent_temperature']:.1f} °C"
        )

        humidity_result.config(
            text=f"{current['relative_humidity_2m']}%"
        )

        pressure_result.config(
            text=f"{current['surface_pressure']:.1f} hPa"
        )

        wind_result.config(
            text=f"{current['wind_speed_10m']:.1f} km/h"
        )

        description_result.config(
            text=weather_description(
                current["weather_code"]
            )
        )

    except ValueError as error:
        messagebox.showerror(
            "Weather Error",
            str(error)
        )

    except requests.RequestException:
        messagebox.showerror(
            "Connection Error",
            "Unable to retrieve weather data.\n"
            "Please check your internet connection and try again."
        )

    except (KeyError, TypeError):
        messagebox.showerror(
            "Data Error",
            "The weather service returned unexpected data."
        )


def clear_weather():
    city_entry.delete(0, tk.END)

    city_result.config(text="--")
    temperature_result.config(text="--")
    feels_result.config(text="--")
    humidity_result.config(text="--")
    pressure_result.config(text="--")
    wind_result.config(text="--")
    description_result.config(text="--")

    city_entry.focus_set()


root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("520x430")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="Weather Dashboard",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=(20, 15))


search_frame = tk.Frame(root)
search_frame.pack(pady=5)


city_entry = tk.Entry(
    search_frame,
    width=28,
    font=("Arial", 12)
)
city_entry.grid(row=0, column=0, padx=5)


search_button = tk.Button(
    search_frame,
    text="Get Weather",
    command=display_weather,
    width=12
)
search_button.grid(row=0, column=1, padx=5)


clear_button = tk.Button(
    search_frame,
    text="Clear",
    command=clear_weather,
    width=10
)
clear_button.grid(row=0, column=2, padx=5)


results_frame = tk.Frame(root)
results_frame.pack(pady=20)


result_labels = [
    "Location",
    "Temperature",
    "Feels Like",
    "Humidity",
    "Pressure",
    "Wind Speed",
    "Condition"
]


result_widgets = []

for row, label_text in enumerate(result_labels):
    label = tk.Label(
        results_frame,
        text=f"{label_text}:",
        font=("Arial", 11, "bold"),
        width=15,
        anchor="e"
    )
    label.grid(
        row=row,
        column=0,
        padx=10,
        pady=5
    )

    value = tk.Label(
        results_frame,
        text="--",
        width=27,
        anchor="w"
    )
    value.grid(
        row=row,
        column=1,
        padx=10,
        pady=5
    )

    result_widgets.append(value)


(
    city_result,
    temperature_result,
    feels_result,
    humidity_result,
    pressure_result,
    wind_result,
    description_result
) = result_widgets


city_entry.focus_set()


root.mainloop()
