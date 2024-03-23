import requests

def api_call(index, name):
    url = f"https://www.dnd5eapi.co/api/{index}/{name}"
    payload = {}
    headers = {
      'Accept': 'application/json'
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Call the function and print the result
    result = api_call(index, name)
    print(result)