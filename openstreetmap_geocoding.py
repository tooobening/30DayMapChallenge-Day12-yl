import requests
import json
def search_location(query: str) -> dict:
    """parameter using for querying"""
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': query,
        'format': 'json',
        'limit': 1,
        'addressdetails': 1
    }
    headers = {
        'User-Agent': 'YourApp/1.0'
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data:
            return data[0]
        return None

    except Exception as e:
        print(f"Error searching for {query}: {e}")
        return None

if __name__ == "__main__":
    search_location()
