from dataclasses import dataclass
from datetime import datetime


'''In Python, a dataclass is a decorator 
(@dataclass) that automatically adds special methods to a class, such as __init__, __repr__, __eq__, 
and others, based on the class attributes you define. It was introduced in Python 3.7 
to make writing classes that primarily store data cleaner and more concise.
__init__: Constructor Method
__eq__: Equality Comparison
__repr__: Official String Representation
'''

'''An immutable object in Python is an object whose state cannot be changed after it is created'''

@dataclass
class User:
    id: int = None
    email: str = ""
    password: str = ""
    createdby: str = ""
    createdat: datetime = None
    updatedby: str = ""
    updatedat: datetime = None