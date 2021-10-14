from pyowm import OWM

while True:
    city_name = input('\nPlease input city name in format "<city>,<Country_Index>" to get weather data, for example: '
                      'Milan,IT.\nPlease write a city name: ')
    owm = OWM('0ec57f389f38e848202eafdc9373c18e')  # You MUST provide a valid API key
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(f'{city_name}')
    w = observation.weather
    user_choice = int(input('\nWhat would you like to know?\n1.Detailed Status\n2.Wind\n3.Humidity\n4.Temperature\n'
                            '5.Rain\n6.Heat index\n7.Clouds\n8.All of the above\n9.Exit\nPlease choose from 1 to 9: '))
    if user_choice == 1:
        print(w.detailed_status)
    elif user_choice == 2:
        print(w.wind())
    elif user_choice == 3:
        print(w.humidity)
    elif user_choice == 4:
        print(w.temperature('celsius'))
    elif user_choice == 5:
        print(w.rain)
    elif user_choice == 6:
        print(w.heat_index)
    elif user_choice == 7:
        print(w.clouds)
    elif user_choice == 8:
        print()
        print("Detailed Status: ", w.detailed_status)
        print("Wind: ", w.wind())
        print("Humidity: ", w.humidity)
        print("Temperature: ", w.temperature('celsius'))
        print("Rain: ", w.rain)
        print("Heat index: ", w.heat_index)
        print("Clouds: ", w.clouds)
    elif user_choice == 9:
        break
    else:
        break
