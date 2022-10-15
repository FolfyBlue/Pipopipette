# <========== Import ==========>

from __future__ import annotations

# <========== Class ==========>

class Score():

    # <----- init ----->

    def __init__(self: Score, x: int = 0) -> None: self.__value: int  = x

    # <----- getter ----->

    @property
    def score(self: Score) -> int: return self.__value

    # <----- setter ----->

    @score.setter
    def score(self: Score, newScore: int) -> None: self.__value = newScore

    # <----- operateur ----->

    def __iadd__(self: Score, x:int) -> Score: return Score(self.__value + x)

    def __add__(self: Score, x: int) -> Score: return Score(self.__value + x)

    def __isub__(self: Score, x:int) -> Score: return Score(self.__value - x)

    def __sub__(self: Score, x: int) -> Score: return Score(self.__value - x)

    # <----- comparateur ----->

    def __eq__(self: Score, other: Score) -> bool: return self.__value == other.__value

    def __ne__(self: Score, other: Score) -> bool: return self.__value != other.__value
    
    def __lt__(self: Score, other: Score) -> bool: return self.__value < other.__value
    
    def __gt__(self: Score, other: Score) -> bool: return self.__value > other.__value
    
    def __le__(self: Score, other: Score) -> bool: return self.__value <= other.__value
    
    def __ge__(self: Score, other: Score) -> bool: return self.__value >= other.__value

    # <----- str ----->

    def __str__(self: Score) -> str: return f"score is {self.__value}."
        
