import requests
import time

time.sleep(5)

url = 'http://127.0.0.1:5000/delete_user'
params = {'user_id': 'USER_ID', 'token': 'TOKEN'}
# params = {'user_id': 'johndoe123'}

response = requests.delete(url, params=params)

if response.json():
    print(response.json())
elif response.status_code == 204:
    print("User deleted successfully.")
elif response.status_code == 401:
    print("Authentication failed. Check your token.")
elif response.status_code == 404:
    print("User not found.")
else:
    print(f"Failed to delete user. Status code: {response.status_code}")




