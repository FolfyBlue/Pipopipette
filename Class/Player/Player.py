# <========== Import ==========>

from __future__ import annotations
from typing import Final
from Score import Score

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
        self.__NAME: Final[str] = name
        self.__ID: Final[int] = id
        self.__score: Score = Score()
    
    # <----- getter -----> 
    
    @property
    def NAME(self: Player) -> str: return self.__NAME
    """
    Define the name of this player
    """

    @property
    def ID(self: Player) -> int: return self.__ID
    
    @property
    def score(self: Player) -> Score: return self.__score
    
    # <----- setter ----->
    
    @score.setter
    def score(self: Player, newScore: int) -> None: self.__score = Score(newScore)
    
    # <----- str ----->
    
    def __str__(self: Player) -> str: return f"{self.__NAME} {self.__score}"