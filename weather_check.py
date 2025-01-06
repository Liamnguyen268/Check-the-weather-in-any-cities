import requests

def get_weather(city_name, api_key):
    base_url= "https://api.openweathermap.org/data/2.5/weather?"
    complete_url= base_url+"q="+city_name+"&appid="+api_key+"&units=metric"    
    try:
        response= requests.get(complete_url)
        response.raise_for_status()  
        data= response.json()
        #print("API Response Data:", data)  

        if data["cod"] != "404":
            main=data["main"]
            weather=data["weather"][0]
            temp= main["temp"]
            humidity=main["humidity"]
            description=weather["description"]
            print(f"Weather in {city_name.capitalize()}:")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description.capitalize()}")
        else:
            print("City not found. Please enter a valid city name.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    city_name= input("Enter city name: ")
    api_key= "eb2d34b1e9b26296105d25e64ec64601" 
    get_weather(city_name, api_key)


