# <========== import ==========>

from __future__ import annotations

# <========== class ==========>

class Segment():
    
    # <----- init ----->
    
    def __init__(self: Segment, ownerID: int = -1) -> None:
        self.__ownerID: int = ownerID
        
    # <----- getter ----->
    
    @property
    def ownerID(self: Segment) -> int: return self.__ownerID
    
    # <----- setter ----->
    
    @ownerID.setter
    def ownerID(self: Segment, ownerID: int) -> None: self.__ownerID = ownerID
        