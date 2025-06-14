import requests

def get_weather(city, unit='imperial'):
    api_key="6d306c01db44f9bb5a50a6912e99d511"  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&APPID={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 404:
        return None
    return response.json()

def display_weather(data,unit):
    if data:
        weather = data['weather'][0]['main']
        temp = round(data['main']['temp'])
        unit_symbol = '°F' if unit == 'imperial' else '°C'
        print(f"The weather in {data['name']} is: {weather}")
        print(f"The temperature in {data['name']} is: {temp} {unit_symbol}")
    else:
        print("No city found. Please try again.")

def user_input():
    city = input("Please enter your city: ")
    unit_choice = input("Choose unit (C for Celsius, F for Fahrenheit): ").strip().upper()
    unit = 'metric' if unit_choice == 'C' else 'imperial'
    
    weather_data = get_weather(city, unit)
    display_weather(weather_data,unit)

if __name__ == "__main__":
    user_input()  # Call the main function to run the program
