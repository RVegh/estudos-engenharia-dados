import requests

url = 'https://pokeapi.co/api/v2/pokemon/ditto'

#Get data from http request
response = requests.get(url)
#response = requests.get(url).json() return response as json object

#Show the url
print(response.url)

#Show de http status code
print(response.status_code)

#Show the content of the request
print(response.content)



