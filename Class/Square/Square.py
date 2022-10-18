# <========== import ==========>

from __future__ import annotations
from Square.Segment import Segment

# <========== class ==========>

class Square:
    """
    Create a new Square.
    """
    
    # <----- init ----->
    
    def __init__(self: Square, id = 0) -> None:
        """
        Args:
            id: The ID of this square.
        """
        self.__left: Segment = Segment()
        self.__right: Segment = Segment()
        self.__top: Segment = Segment()
        self.__down: Segment = Segment()
        self.__squareOwner: int = -1
        self.__id: int = id
        
    # <----- getter ----->
    
    @property
    def left(self: Square) -> Segment: return self.__left
    
    @property
    def right(self: Square) -> Segment: return self.__right
    
    @property
    def top(self: Square) -> Segment: return self.__top
    
    @property
    def down(self: Square) -> Segment: return self.__down
    
    @property
    def squareOwner(self: Square) -> int: return self.__squareOwner
    
    @property
    def id(self: Square) -> int: return self.__id
    
    # <----- setter ----->
    
    @left.setter
    def left(self: Square, owner: int) -> None: 
        self.__left.ownerID = owner
        if self.__right.ownerID != -1 and self.__top.ownerID != -1 and self.__down.ownerID != -1: self.__squareOwner.ownerID = owner
    
    @right.setter
    def right(self: Square, owner: int) -> None: 
        self.__right.ownerID = owner
        if self.__left.ownerID != -1 and self.__top.ownerID != -1 and self.__down.ownerID != -1: self.__squareOwner.ownerID = owner
    
    @top.setter
    def top(self: Square, owner: int) -> None: 
        self.__top.ownerID = owner
        if self.__right.ownerID != -1 and self.__left.ownerID != -1 and self.__down.ownerID != -1: self.__squareOwner.ownerID = owner
    
    @down.setter
    def down(self: Square, owner: int) -> None: 
        self.__down.ownerID = owner
        if self.__right.ownerID != -1 and self.__top.ownerID != -1 and self.__left.ownerID != -1: self.__squareOwner.ownerID = owner
        
    @squareOwner.setter
    def squareOwner(self: Square, owner: int) -> None: self.__squareOwner = owner
    
    @id.setter
    def id(self: Square, owner: int) -> None: self.__squareOwner = owner  
      
    # <----- str ----->
    
    def __str__(self: Square) -> str: return f"[id:{self.__id}(l:{self.__left.ownerID},r:{self.__right.ownerID},t{self.__top.ownerID},d{self.__down.ownerID}), owner:{self.__squareOwner}]"   