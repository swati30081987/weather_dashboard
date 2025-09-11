# filepath: [weather_dashboard.py](http://_vscodecontentref_/0)
import streamlit as st # type: ignore
import requests
import os
from dotenv import load_dotenv
load_dotenv() # Loads variables from .env file into os.environ
API_KEY = os.getenv('API_KEY')

st.title("Weather Dashboard")

city = st.text_input("Enter city name", "New York")

if st.button("Get Weather"):
    url = (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        f"{city}?unitGroup=metric&key={API_KEY}&contentType=json"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Get today's weather
        today = data['days'][0]
        st.subheader(f"Weather in {city} ({today['datetime']})")
        st.write(f"**Temperature:** {today['temp']} °F")
        st.write(f"**Conditions:** {today['conditions']}")
        st.write(f"**Humidity:** {today['humidity']}%")
        st.write(f"**Wind Speed:** {today['windspeed']} km/h")
    else:
        st.error("City not found or API error.")