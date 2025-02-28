# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a dict
person = {
    'first_name': 'Joao',
    'last_name' : 'Bro',
    'age': 25
}

# Get a value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict Items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Vila'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length (key/value pairs)
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age' : 30},
    {'name': 'Kevin', 'age' : 25}
]

print(people[1]['name'])

print(person, type(person))