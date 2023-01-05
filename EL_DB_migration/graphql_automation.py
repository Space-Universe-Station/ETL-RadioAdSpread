import requests

# Set the endpoint URL
URL = "http://localhost:5000/api/v3"
# Set the headers
headers = {
    "Content-Type": "application/json"
}

def BulkRegisterBroadcasters(country, fullname, name,positionHeld,address,state,city,radioStationWebsite,radioStationDigitalStreaUrl,radioStationCategory,phoneNumber,email,password,url=URL,header=headers):
  # Set the GraphQL query
  query = """
  mutation Mutation($input: BroadcasterRegisterInput) {
    auth {
      broadcasterRegister(input: $input) {
        token
      }
    }
  }
  """
  # Set the variables
  variables = {
      "input": {
          "address": address,
          "city": city,
          "confirmPassword": password,
          "country": country,
          "email": email,
          "fullname": fullname,
          "name": name,
          "password": password,
          "phoneNumber": phoneNumber,
          "positionHeld": positionHeld,
          "radioStationCategory": radioStationCategory,
          "radioStationWebsite": radioStationWebsite,
          "radioStationDigitalStreaUrl": radioStationDigitalStreaUrl,
          "state": state
      }
  }
  # Set the payload
  payload = {
      "query": query,
      "variables": variables
  }
  # Send the POST request
  response = requests.post(url, json=payload, headers=header)
  # Print the response
  print(response.json())
