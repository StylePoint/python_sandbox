# A module is basically a file containing a set of functions to include in your application. There are core python modules, 
# modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
from sqlite3 import Timestamp

today = datetime.date.today()

print(today)

# Import just the "date" part of "datetime"
from datetime import date
print(date.today())

# Import time
import time
timestamp = time.time()

# Or just time
from time import time
timestamp = time()

# To install modules (same as npm i wtv) you do pip install wtv
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there'))

# Import custom modules (aka. other files) (this one is validator.py)
from validator import validate_email

email ='teste@teste.com'
if validate_email(email):
    print('email is valid')