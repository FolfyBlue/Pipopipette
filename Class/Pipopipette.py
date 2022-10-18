# <========== Import ==========>

from __future__ import annotations
from typing import Final
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
        self.__width: Final[int] = width
        self.__height: Final[int] = height
        self.__list_square: list[Square] = []

        for i in range(width * height): self.__list_square.append(Square(i))

    # <----- getter ----->

    @property
    def width(self: Pipopipette) -> int: return self.__width

    @property
    def height(self: Pipopipette) -> int: return self.__height

    @property
    def list_square(self: Pipopipette) -> list[Square]: return self.__list_square

    # <----- setter ----->

    @list_square.setter
    def list_square(self: Pipopipette, newlist_square: list[Square]) -> None: self.__list_square = newlist_square.copy()

    # <----- str ----->

    def __str__(self: Pipopipette) -> str:
        return_str = ""
        for square in self.__list_square: return_str += square.__str__() + " "
        return return_str

     # <----- get_square_by_ID ----->

    def get_square_by_ID(self: Pipopipette, id: int) -> Square | None:
        """
        Used to get a Square by his ID
        Args:
            id: A Square's id

        Returns:
            The found square, or None
        """
        for square in self.__list_square:
            if square.id == id: return square
        return None

    # <----- setSide ----->

    def set_side(self: Pipopipette, squareID: int, side: str, owner_ID: int) -> None:
        """Defines the owner of a side of a square.

        Args:
            squareID (int): ID of the square to edit.
            side (str): 'l', 'r', 't', or 'd'. Side to edit.
            owner_ID (int): ID Of the player who now owns this side.
        """
        if (square := self.get_square_by_ID(squareID)) != None:
            match side:
                case 'l':
                    square.left.owner_ID = owner_ID
                    if (neighbor := self.get_square_by_ID(squareID-1)) != None:
                        neighbor.right.owner_ID = owner_ID
                case 'r':
                    square.right.owner_ID = owner_ID
                    if (neighbor := self.get_square_by_ID(squareID+1)) != None:
                        neighbor.left.owner_ID = owner_ID
                case 't':
                    square.top.owner_ID = owner_ID
                    if (neighbor := self.get_square_by_ID(squareID-self.__height)) != None:
                        neighbor.down.owner_ID = owner_ID
                case 'd':
                    square.down.owner_ID = owner_ID
                    if (neighbor := self.get_square_by_ID(squareID+self.__height)) != None:
                        neighbor.top.owner_ID = owner_ID

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
        if self.get_square_by_ID(squareID) != None:
            if ((side == 'l' and self.get_square_by_ID(squareID).left.owner_ID != -1) or
                (side == 'r' and self.get_square_by_ID(squareID).right.owner_ID != -1) or
                (side == 't' and self.get_square_by_ID(squareID).top.owner_ID != -1) or
                (side == 'd' and self.get_square_by_ID(squareID).down.owner_ID != -1)): return True
        return False