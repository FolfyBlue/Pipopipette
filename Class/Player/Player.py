# <========== Import ==========>

from __future__ import annotations
from Player.Score import Score

# <========== Class ==========>

class Player():
    """
    Represent the player. This class holds all the methods that allow the player to interact with the game.
    """
    
    # <----- init ----->
    
    def __init__(self: Player, name: str, id: int) -> None:
        """"
        Create a new player.
        Args:
            name (str): The name of this user.
            id (int): An unique identifier for this user.
        """
        self.__name: str = name
        self.__id = id
        self.__score: Score = Score()
    
    # <----- getter -----> 
    
    @property
    def name(self: Player) -> str: return self.__name
    """
    Define the name of this player
    """

    @property
    def id(self: Player) -> int: return self.__id
    
    @property
    def score(self: Player) -> Score: return self.__score
    
    # <----- setter ----->
    
    @name.setter
    def name(self: Player, newName: str) -> None: self.__name = newName

    @id.setter
    def id(self: Player, newID: int) -> None: self.__id = newID
    
    @score.setter
    def score(self: Player, newScore: int) -> None: self.__score = Score(newScore)
    
    # <----- str ----->
    
    def __str__(self: Player) -> str: return f"{self.__name} {self.__score}"