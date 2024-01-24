import requests
import xmltodict
import json

# Function to convert XML data to JSON
def xml_to_json(xml_data):
    dict_data = xmltodict.parse(xml_data)
    json_data = json.dumps(dict_data)
    return json_data

# Function to send data to Grafana
def send_to_grafana(json_data, grafana_url, api_token):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(grafana_url, headers=headers, data=json_data)
    return response

# Downloading the file (assuming it's XML in this case)
file_url = "http://35.174.18.150:8080/job/src/8/execution/node/3/ws/cppcheck-results.txt"
response = requests.get(file_url)

with open('check.xml', 'w') as file:
    file.write(response.text)

# Convert XML to JSON
with open('check.xml', 'r') as file:
    xml_content = file.read()
    json_data = xml_to_json(xml_content)

# Grafana details (modify with your actual values)
grafana_url = 'http://35.174.18.150:3000/connections/datasources/new'
api_token = 'glsa_QWnOyjlCZnMYFRyBLDKyn0pTEQ2zMhme_ffa43c32'

# Send the JSON data to Grafana
response = send_to_grafana(json_data, grafana_url, api_token)

# Print the response from Grafana
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
