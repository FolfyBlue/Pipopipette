# <========== Import ==========>

from __future__ import annotations
from Square.Square import Square

# <========== Class ==========>

class Pipopipette():
    """
    The class that will manage the playground.
    """
    
    # <----- init ----->
    
    def __init__(self: Pipopipette, width: int = 5, height: int = 5) -> None:
        """

        Args:
            width: The width of the game
            height: The height of the game
        """
        self.__width: int = width
        self.__height: int = height
        self.__listSquare: list[Square] = []
        
        for i in range(width * height): self.__listSquare.append(Square(i))
    
    # <----- getter ----->
    
    @property
    def width(self: Pipopipette) -> int: return self.__width
    
    @property
    def height(self: Pipopipette) -> int: return self.__height
    
    @property
    def listSquare(self: Pipopipette) -> list[Square]: return self.__listSquare
    
    # <----- setter ----->
    
    @width.setter
    def width(self: Pipopipette, newwidth: int) -> None: self.__width = newwidth
    
    @height.setter
    def height(self: Pipopipette, newheight: int) -> None: self.__height = newheight

    @listSquare.setter
    def listSquare(self: Pipopipette, newlistSquare: list[Square]) -> None: self.__listSquare = newlistSquare.copy()

    # <----- str ----->

    def __str__(self: Pipopipette) -> str:
        rstr = ""
        for square in self.__listSquare: rstr += square.__str__() + " "
        return rstr
    
     # <----- getSquareByID ----->
    
    def get_square_by_ID(self: Pipopipette, id: int) -> Square | None:
        """
        Used to get a Square by his ID
        Args:
            id: A Square's id

        Returns:
            The found square, or None
        """
        for square in self.__listSquare:
            if square.id == id: return square
        return None
    
    # <----- setSide ----->
    
    def set_side(self: Pipopipette, squareID: int, side: str, ownerID: int) ->  None:
        """
        Define the side of a Square.
        Args:
            squareID: The ID of the Squre to edit
            side: 'l'; 'r', 't', or 'd'. Wich side to edit ?
            ownerID: The player who placed this side

        """
        if self.getSquareByID(squareID) != None: 
            if side == 'l':
                self.getSquareByID(squareID).leftOwner = ownerID
                if self.getSquareByID(squareID-1) != None: self.getSquareByID(squareID-1).rightOwner = ownerID
            elif side == 'r':
                self.getSquareByID(squareID).rightOwner = ownerID
                if self.getSquareByID(squareID+1) != None: self.getSquareByID(squareID+1).leftOwner = ownerID
            elif side == 't':
                self.getSquareByID(squareID).topOwner = ownerID
                if self.getSquareByID(squareID-self.__height) != None: self.getSquareByID(squareID-self.__height).downOwner = ownerID
            elif side == 'd':
                self.getSquareByID(squareID).downOwner = ownerID
                if self.getSquareByID(squareID+self.__height) != None: self.getSquareByID(squareID+self.__height).topOwner = ownerID
            
    # <----- valideTarget ----->
    
    def valid_target(self: Pipopipette, squareID: int, side: str) -> bool:
        """
        Can a player place a Segment here ?
        Args:
            squareID: The square to check
            side: The side to check. 'l', 'r', 't' or 'd'

        Returns:
            Boolean - True if can edit, False if already owned by a player

        """
        if self.getSquareByID(squareID) != None:
            if ((side == 'l' and self.getSquareByID(squareID).leftOwner != -1) or
                (side == 'r' and self.getSquareByID(squareID).rightOwner != -1) or
                (side == 't' and self.getSquareByID(squareID).topOwner != -1) or
                (side == 'd' and self.getSquareByID(squareID).downOwner != -1)): return True
        return False 