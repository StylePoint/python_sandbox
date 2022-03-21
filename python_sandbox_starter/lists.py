# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1,2,3,4,5]
fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Use constructor 
nubmers2 = list((1,2,3,4,5))


# Get a value (lists start on 0)
print(fruits[1])

# Get Length
print(len(fruits))

# Append to list
fruits.append("Mangos")

# Remove from list
fruits.remove("Grapes")

# Change value
fruits[0] = "Blueberries"

# Insert into specific position
fruits.insert(2, "Strawberries")

# Remove from specific position
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort 
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)