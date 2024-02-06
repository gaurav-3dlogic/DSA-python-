# Make a GET request to this endpoint ”https://jsonplaceholder.typicode.com/posts”. And print all values for the key “title”.
import requests

# Make the GET request
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the JSON response data
    data = response.json()

    # Extract and print the values for the key "title"
    for item in data:
        title = item["title"]
        print(title)
else:
    print("Error:", response.status_code)