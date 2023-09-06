import requests
import time

time.sleep(5)

url = 'http://127.0.0.1:5000/delete_user'
params = {'user_id': 'johndoe123', 'token': 'f146983f08669dfdfd9e4ad5b9e25b48'}
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




