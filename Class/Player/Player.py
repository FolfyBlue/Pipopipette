# <========== Import ==========>

from __future__ import annotations
from Player.Score import Score

# <========== Class ==========>

class Player():
    
    # <----- init ----->
    
    def __init__(self: Player, name: str, id: int) -> None:
        self.__name: str = name
        self.__id = id
        self.__score: Score = Score()
    
    # <----- getter -----> 
    
    @property
    def name(self: Player) -> str: return self.__name

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