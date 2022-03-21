# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'My name is {self.name}'
    def has_birthday(self):
        self.age += 1

# Init user object
joao = User('Joao costa', 'teste@teste.com', 25)

# Get object variable
print(joao.name)

# User object method
print(joao.greeting())
joao.has_birthday()
print(joao.age)

# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, value):
        self.balance = value
    # Override method (if we didnt overide we could still use the greeting method normally)
    def greeting(self):
        return f'My name is {self.name} and my balance is {self.balance}'

# Init customer
luce = Customer("Luce Puce", "luce@mail.com", 25)
luce.set_balance(13)
# Using parent method
luce.has_birthday()
print(luce.balance)