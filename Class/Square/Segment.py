# <========== import ==========>

from __future__ import annotations

# <========== class ==========>

class Segment():
    """
    Used to represent a segment, placed by a player.
    """
    
    # <----- init ----->
    
    def __init__(self: Segment, ownerID: int = -1) -> None:
        """
            Create a new Segment
            Args:
                ownerID (int): The ID of the user who placed this. Default to -1 for no owner
        """
        self.__ownerID: int = ownerID
        
    # <----- getter ----->
    
    @property
    def ownerID(self: Segment) -> int: return self.__ownerID
    
    # <----- setter ----->
    
    @ownerID.setter
    def ownerID(self: Segment, ownerID: int) -> None: self.__ownerID = ownerID
        