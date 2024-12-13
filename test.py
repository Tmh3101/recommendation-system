import requests

url = 'http://127.0.0.1:8000/recommend'

# Tạo payload JSON
input_data = {'movie_name': 'Iron Man'}

# Gửi yêu cầu POST với JSON payload
response = requests.post(url, json=input_data)

# In kết quả
if response.status_code == 200:
    print(response.json())
else:
    print(f'Error: {response.status_code} - {response.text}')
