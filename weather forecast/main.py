import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")

        self.label = tk.Label(root, text="Enter City or Zip Code:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.button.pack()

        self.result_label = tk.Label(root, text="", wraplength=300)
        self.result_label.pack()

    def get_weather(self):
        user_input = self.entry.get()
        weather_data = self.fetch_weather_data(user_input)

        if weather_data:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            description = weather_data['weather'][0]['description']

            result_text = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {description}"
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="City or Zip Code not found")

    def fetch_weather_data(self, user_input):
        api_key = "PMAK-64d51710c8f401003190982a-83987d95e712c2ac9baad6157957015aa1"
        base_url = "http://api.openweathermap.org/data/2.5//forecast?appid=<string>&q=<string>&id=<integer>&lat=<number>&lon=<number>&zip=<string>&units=<string>&lang=<string>&Mode=<string>"
        params = {
            "q": user_input,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            return None

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
