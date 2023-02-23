# PYTHON DOES NOT PROVIDE ABSTRACT CLASSES

# Abstract Base class (ABC) -- Python comes with a module that provides the base for defining abstract base classes (ABC) and that module name is ABC

from abc import ABC, abstractmethod
from asyncio.windows_events import proactor_events
from pyclbr import Class

# Python program showing
# abstract properties
 
import abc
from abc import ABC, abstractmethod
 
class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"


class child(parent):
      
    @property
    def geeks(self):
        return "child class"
  
  
try:
    r =parent()
    print( r.geeks)
except Exception as err:
    print (err)
  
r = child()
print (r.geeks)

