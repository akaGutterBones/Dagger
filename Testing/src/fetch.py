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
        if index == "classes":
            result = {key: data[key] for key in ['name', 'hit_die'] if key in data}
            if 'proficiency_choices' in data:
                result['proficiency_choices'] = [item['desc'] for item in data['proficiency_choices'] if 'desc' in item]
            return result
        else:
            return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None