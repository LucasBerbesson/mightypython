"""Snippet to generate a 8 to 16 characters long password
"""
import string
from random import *

characters = string.ascii_letters+string.punctuation+string.digits
password  =   "".join(choice(characters) for x in range(randint(8, 16)))
print(password)
