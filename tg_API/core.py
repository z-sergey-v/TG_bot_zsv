import requests



url = "https://numbersapi.p.rapidapi.com/6/21/date"

querystring = {"fragment":"true","json":"true"}

headers = {
	"X-RapidAPI-Key": "4a99619c73msh7cf01c25688c1a5p14fb8bjsnf7a248fd5ebc",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)