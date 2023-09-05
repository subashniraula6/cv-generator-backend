import requests

url = 'http://localhost:5000/delete_user'
params = {'user_id': 'user_id', 'token': 'TOKEN'}

response = requests.delete(url, params=params)
print(response.json())
