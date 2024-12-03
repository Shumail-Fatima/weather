import requests
import pandas as pd


city_name = 'karachi'
API_key = '092575f84681c1fd4f2f6258d443790e'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

get_site_info = requests.get(url)
if get_site_info.status_code == 200:
    data = get_site_info.json()
    #print(data)


fields = {
    "Weather Description": data['weather'][0]['description'],
    "Temperature (°C)": data['main']['temp'],
    "Feels Like (°C)": data['main']['feels_like'],
    "Pressure (hPa)": data['main']['pressure'],
    "Humidity (%)": data['main']['humidity'],
    "Visibility (m)": data['visibility'],
    "Wind Speed (m/s)": data['wind']['speed'],
    "Wind Direction (°)": data['wind']['deg']
}

# Loop to display the information
for key, value in fields.items():
    print(f"{key}: {value}")

pd.DataFrame.from_dict(data=fields, orient='index').to_csv('dict_file.csv', header=False)