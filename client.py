import requests

SERVER_URL = "http://localhost:8080"

def call_api(endpoint, payload):
    try:
        response = requests.post(
            f"{SERVER_URL}/{endpoint}",
            json=payload,
            timeout=2  # 2-second timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

if __name__ == "__main__":
    # Test add
    result = call_api("add", {"x": 2, "y": 3})
    if result:
        print(f"add(2,3) = {result['result']}")

    # Test multiply
    result = call_api("multiply", {"x": 4, "y": 5})
    if result:
        print(f"multiply(4,5) = {result['result']}")
