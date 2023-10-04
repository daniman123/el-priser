import requests

# Example GET request
url = "https://www.emd-international.com/el/fetch2.php?location=WEST&graph=1&start=2023-10-4&m=0.9042978232096179"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print("Data retrieved successfully:")
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
