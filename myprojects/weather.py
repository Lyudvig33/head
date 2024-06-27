
# Importing the requests module for making HTTP requests
import requests

# Importing the argparse module for parsing command-line arguments
import argparse



# Function to get weather data for a given city using the OpenWeatherMap API
def get_city_data(city):
    try:

        # API token for accessing the OpenWeatherMap API    
        api_token = "e4d6d1f0b51027b7f69dde004f4b4f31"

        # API endpoint URL for weather data
        url = "https://api.openweathermap.org/data/2.5/weather"

        # Parameters for the API request
        params = {
            'q': city,
            'appid': api_token,
            'units': 'metric' #(metric for Celsius))

        }
        
    
        responese = requests.get(url, params=params)

         
        data = responese.json()

         # Handling exceptions (e.g., network error, invalid city name)
    except Exception as ex:
        print(ex)
        print("check the city name")
    return data

# Function to display weather information for a given city
def weather_info(data):
    print(f"Weather in {data['name']}:")
    print(f"Description: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Pressure: {data['main']['pressure']} hPa")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

# Main function to handle command-line arguments and fetch weather information
def main():
    try:

        # Creating an argument parser object
        parser = argparse.ArgumentParser(description="Weather forecast program")

        # Adding command-line arguments
        parser.add_argument("city", help="Name of the city to get weather information for")
        parser.add_argument("--option", "-o", default="" ,choices=["temperature", "pressure", "humidity", "wind_speed"],
                            help="Weather information option to display")
        
        # Parsing the command-line arguments
        args = parser.parse_args()
        city = args.city
        option = args.option
        data = get_city_data(city)
        if option == "":
            print(weather_info(data))
        if option == "temperature":
            print(f"Weather in {data['name']}:")
            print(f"Temperature: {data['main']['temp']}°C")
        elif option == "pressure":
            print(f"Weather in {data['name']}:")
            print(f"Pressure: {data['main']['pressure']} hPa")
        elif option == "humidity":
            print(f"Weather in {data['name']}:")
            print(f"Humidity: {data['main']['humidity']}%")
        elif option == "wind_speed":
            print(f"Weather in {data['name']}:")
            print(f"Wind Speed: {data['wind']['speed']} m/s")


    except Exception as ex:
        print(ex)

# Entry point of the program
if __name__ == '__main__':
    main()







# import requests





# def weather_check(city):
#     api_token = "e4d6d1f0b51027b7f69dde004f4b4f31"
#     url = "https://api.openweathermap.org/data/2.5/weather"
#     params = { 
#         'q': city,
#         'appid': api_token,
#         'units': 'metric'
#     }   
#     responese = requests.get(url,params=params)
#     data = responese.json()
#     country = data['sys']['country']
#     city = data['name']
#     temperature = data['main']['temp']
#     feels_like_temp = data['main']['feels_like']
#     cloud_cover = data['weather'][0]['description']
#     speed_wind = data['wind']['speed']
#     humidity = data['main']['humidity']





    
#     print(f"Country--{country}\nCity--{city}\nTemperature--{temperature}\nFeels_like--{feels_like_temp}\nCloud_Cover--{cloud_cover}\nSpeed_Win--{speed_wind}\nHumidity--{humidity}")
# if __name__=="__main__":
#     print("Current Weather In Your City")
#     city = input("Enter Your City: ")

#     weather_check(city)
corrections = {}
        for word in cnt:
            if word in spell:
                corrrection = spell.correction(word)
                print(f"current word {word},corrected word {corrrection}")
                print(f"variants words:,{spell.candidates(word)}")
                variants = input("Enter your variant, or press Enter to skip  ")
                if variants:
                    corrrection = variants
                corrections[word] = corrrection
            
    corected_text = ' '.join(corrections.get(word,i)for i in cnt)
    
    with open(output_file,'w') as output_file:
        output_file.write(corected_text)
        
    print("Corected text the saved is",output_file)