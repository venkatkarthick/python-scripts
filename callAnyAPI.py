import requests
api_url = "https://api.github.com/users/venkatkarthick"

data = {
}

#response = requests.post(api_url, json=data)
response = requests.get(api_url)

if response.status_code == 200:
    # Parsing the JSON response
    data = response.text
    print("API response data:", data)
else:
    print("Failed to retrieve data:", response.status_code, response.text)
