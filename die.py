""" Sets the number of sides of the die and the value of the rolled 
    die. 
    Attributes: 
    sides (int): number of sides on die 
    value (int): returned value from roll"""

import random 
class Die:
  
  def __init__(self, sides = 6): 
    """ Initializes the die side and value. """
    self.sides = sides
    self.value = 0

  def roll(self):
    """ Function randomly rolls the die. """
    self.value = random.randint(1, self.sides)
    return self.value 

  def __str__(self):
    """ Returns the die value as a string. """
    return str(self.value)

  def __lt__(self, other):
    """ Compares if one die's value is less than the other using <. 
 """
    return self.value < other.value

  def __eq__(self, other):
    """ Compares if one die's value is equal to the others. """
    return self.value == other.value

  def __sub__(self, other):
    """ Gets the difference between the values of 2 dice. """
    return abs(self.value - other.value)
    