import requests
def fetch_date(api):
    try:
        response = requests.get(api)
        response.raise_for_status()  # Check if the request was successful
        return response.json()  # Return the JSON data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

