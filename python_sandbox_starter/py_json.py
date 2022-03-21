# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# Sample JSON
userJSON = '{"first_name" : "Joao", "last_name": "Costa", "age": 25}'

# Parse into dict
user = json.loads(userJSON)

print(user['age'])

# Convert to JSON
car = {"model" : "ford", "make": "wat", "year": 25}

carJSON = json.dumps(car)

print(carJSON)