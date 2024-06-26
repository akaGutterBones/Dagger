import requests, json

def api_call(index, name):
    url = f"https://www.dnd5eapi.co/api/{index}/{name}"
    payload = {}
    headers = {
      'Accept': 'application/json'
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None