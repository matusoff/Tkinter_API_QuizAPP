import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean") 
response.raise_for_status()
data = response.json()
question_data = data["results"]



# parameters = {
#     "amount": 10,
#     "type" : "boolean",
#     "category": 18

# }

# response = requests.get(url="https://opentdb.com/api.php", params=parameters) 
# response.raise_for_status()
# data = response.json()
# question_data = data["results"]


