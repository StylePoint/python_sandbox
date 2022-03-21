# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ("Apples", "Oranges", "Grapes")
#fruits2 = tuple(("Apples", "Oranges", "Grapes"))

# Single value needs trailing comma
fruits2 = ("Apples",)

# Can't change value
#fruits[0] = "Pears"

# Delete tuple
del fruits2

print(fruits)
 


# A Set is a collection which is unordered and unindexed. No duplicate members.


# Create a set
fruits_set = {"Apples", "Oranges", "Grapes"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("Mango")

# Remove from set
fruits_set.remove("Grapes")

# Add duplicate (duplicates dont give error, just dont work)
fruits_set.add("Apples")


# Clear set
#fruits_set.clear()

# Delete
#del fruits_set

print(fruits_set)