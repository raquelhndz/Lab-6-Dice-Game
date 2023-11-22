""" Creates a list of 3 Die objects and manages the player’s points. 
    Attributes:
    dice (Die list): list of 3 die objects 
    points (int): players point """

import die
class Player: 
  def __init__(self):
    """ Constructs and sorts the list of three Die objects and initializes the player’s points to 0. """
    
    self.dice = [die.Die(), die.Die(), die.Die()] #composition- owns objects of class 'Die'
    self.points = 0

  def get_points(self):
    """ Returns the player’s points. """
    
    return self.points 

  def roll_dice(self):
    """ Calls roll on each of the Die objects in the dice list and sorts the list. """
    
    for d in self.dice:
      d.roll()
    self.dice.sort()

  def has_pair(self):
    """ Returns true if two dice in the list have the same value (uses ==).Increments points by 1. """ 

    if self.dice[0] != self.dice[1] or self.dice[0] != self.dice[2] or self.dice[1] != self.dice[2]:
      if self.dice[0]== self.dice[1]:
        self.points += 1
        return True
      elif self.dice[0]== self.dice[2]:
        self.points += 1
        return True
      elif self.dice[1] == self.dice[2]:
        self.points += 1
        return True
    return False 

  def has_three_of_a_kind(self):
    """ Returns true if all three dice in the list have the same 
value (uses ==).  Increments points by 3. """
    
    if self.dice[0] == self.dice[1] == self.dice[2]:
      self.points +=3
      return True
    return False
      

  def has_series(self):
    """ Returns true if the values of each of the dice in the list are in a sequence.Increments points by 2. """
    
    if self.dice[2] - self.dice[1] == 1 and self.dice[1] - self.dice[0] == 1:
      self.points+=2
      return True
      
    return False

  def __str__(self):
    """ Returns a formatted string. """
    s = ""
    for i, d in enumerate(self.dice):
      s += "D" + str(i+1) + "=" + str(d) + " "
    return s

  