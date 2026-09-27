# Weather Dashboard

A Python desktop weather application built with Tkinter that retrieves current weather information for any city using the Open-Meteo API.

## Features

- Search weather by city name
- Displays city and country
- Current temperature
- Feels-like temperature
- Relative humidity
- Surface pressure
- Wind speed
- Weather condition
- Handles invalid city names
- Handles empty input
- Handles network connection errors
- Clear button to reset weather information
- No API key required

## Requirements

- Python 3.8 or later
- `requests` Python package
- Internet connection

## Installation

Install the required Python package:

    python -m pip install requests

## How to Run

Open a terminal in the project folder and run:

    python weatherapp.py

## How to Use

1. Start the application.
2. Enter a city name in the search box.
3. Click **Get Weather**.
4. The application retrieves and displays the current weather information.
5. Click **Clear** to reset the displayed information.

## Weather Information

The application displays:

- Location
- Temperature in Celsius
- Feels-like temperature
- Humidity
- Surface pressure
- Wind speed
- Weather condition

## API

This project uses the Open-Meteo API for weather data and its geocoding service to find city coordinates.

Open-Meteo:

https://open-meteo.com/

## Project Structure

    Weather-Dashboard/
    │
    ├── weatherapp.py
    └── README.md

## Technologies Used

- Python
- Tkinter
- Requests
- Open-Meteo API
- GUI Application Development

## Error Handling

The application handles:

- Empty city names
- Invalid city names
- Network connection failures
- API request failures
- Unexpected API responses

## License

This project is provided for educational and personal portfolio purposes.