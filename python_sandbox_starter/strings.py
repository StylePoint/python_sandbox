# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "joao"
age = 25

# Concatonate (you can only concatonate Strings so you have to caste it to str())
print('Hello, my name is ' + name + " and I am "+ str(age))

# Arguments by poistion (we can do placeholders with {} and then use .format to assign them values)
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings use directly the variables
print(f'Hello, my name is {name} and I am {age}')

# String Formatting

# String Methods
s = 'hello world'

# Capitalize string (only capitalizes first letter)
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case (swaps lower to uppercase)
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count (counts substring)
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list 
print(s.split())

# Find position in array
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())


