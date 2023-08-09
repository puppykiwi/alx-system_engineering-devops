import requests

# Set your Datadog API and Application Key
api_key = "c7e15316a1e08c3d1eb54b00451c0a9e"
app_key = "2792847fde543eb0cfddea55f67b9307ccacd420"

# Set the name of the dashboard you want to retrieve the ID for
dashboard_name = "Puppy's Dashboard"

# API endpoint for getting all dashboards
url = "https://api.datadoghq.com/api/v1/dashboard"

# Set headers for the API request
headers = {
    "Content-Type": "application/json",
    "DD-API-KEY": api_key,
    "DD-APPLICATION-KEY": app_key
}

# Make the API request to get all dashboards
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Iterate through the list of dashboards to find the specific dashboard
    for dashboard in data["dashboards"]:
        if dashboard["title"] == dashboard_name:
            dashboard_id = dashboard["id"]
            print(f"Dashboard ID for '{dashboard_name}': {dashboard_id}")
            break
    else:
        print(f"Dashboard '{dashboard_name}' not found.")
else:
    print(f"API request failed with status code: {response.status_code}")
