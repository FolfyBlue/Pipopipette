# <========== Import ==========>

from __future__ import annotations

# <========== Class ==========>

class Score():
    """"
    The Player's score
    """

    # <----- init ----->

    def __init__(self: Score, value: int = 0) -> None:
        """
        Instanciate a new Score.
        Args:
            x (int): The number of points = if this player. Defaults to 0.
        """
        self.__value: int = value

    # <----- getter ----->

    @property
    def value(self: Score) -> int: return self.__value

    # <----- setter ----->

    @value.setter
    def value(self: Score, new_score: int) -> None: self.__value = new_score
    
    def __iadd__(self: Score, x: int) -> None: return Score(self.__value + x)  # type: ignore
    
    def __add__(self: Score, x: int) -> None: return Score(self.__value + x)  # type: ignore
    
    def __isub__(self: Score, x: int) -> None: return Score(self.__value - x)  # type: ignore
    
    def __sub__(self: Score, x: int) -> None: return Score(self.__value - x)  # type: ignore

    # <----- comparateur ----->

    def __eq__(self: Score, other: Score | int) -> bool: 
        if type(other) == Score: return self.__value == other.__value  # type: ignore
        return self.__value == other
        
    def __ne__(self: Score, other: Score | int) -> bool: 
        if type(other) == Score: return self.__value != other.__value  # type: ignore
        return self.__value != other
    
    def __lt__(self: Score, other: Score | int) -> bool:
        if type(other) == Score: return self.__value < other.__value  # type: ignore
        return self.__value < other
    
    def __gt__(self: Score, other: Score | int) -> bool:
        if type(other) == Score: return self.__value > other.__value  # type: ignore
        return self.__value > other
    
    def __le__(self: Score, other: Score | int) -> bool:
        if type(other) == Score: return self.__value <= other.__value  # type: ignore
        return self.__value <= other
    
    def __ge__(self: Score, other: Score | int) -> bool:
        if type(other) == Score: return self.__value >= other.__value  # type: ignore
        return self.__value >= other

    # <----- str ----->

    def __str__(self: Score) -> str: return f"score is {self.__value}."