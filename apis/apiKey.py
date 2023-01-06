import requests

baseUrl = 'https://api.openweathermap.org/data/2.5/forecast'
# TODO: Insert API KEY
parameters = {'appid': 'YOUR_OWN_API_KEY', 'q': 'Torrance,US'}
response = requests.get(baseUrl, params=parameters)

print(response.content)
