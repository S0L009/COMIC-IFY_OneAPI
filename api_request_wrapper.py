import requests

# pip install requests -  if requests not there

# make sure you run the fast-api app in local-host port 8000

chunk_gen = "http://127.0.0.1:8000/gen-chunk" # {"theme": "string", "word_limit": "string", "chunk_content": "string"}
img_gen = "http://127.0.0.1:8000/gen-image" # {"theme": "string"}

# Data to send in the request body (optional)
data = {"theme": "Doraemon", "word_limit": "100", "chunk_content": "Our Environment 209/square6If we add a few aquatic plants and animals it can become a self- sustaining system Which organisms can make organic compounds like sugar and starch from inorganic substances using the radiant energy of the Sun in the presence of chlorophyll? All green plants and certain bacteria which can produce food by photosynthesis come under this categoryand are called the producers.".replace('\n', '')}

def request_wrapper(url, data):
    # Headers (optional)
    headers = {"Content-Type": "application/json"}  # Example for JSON data

    # Send the POST request
    response = requests.post(url, json=data, headers=headers)

    # Check the response status code
    if response.status_code == 200:
    # Request successful, process the response data
        data = response.json()
        return data
    else:
    # Handle error
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    print(request_wrapper(img_gen, {'theme': "Wild-Life"}))
