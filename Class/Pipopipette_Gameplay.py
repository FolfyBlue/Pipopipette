# <========== Import ==========>

from __future__ import annotations
from typing import Final
from Pipopipette import Pipopipette
from Player.Player import Player

# <========== Class ==========>

class Pipopipette_Gameplay():
    """
    Class used to manage the players, their score, ect...
    """
    
    # <----- init ----->
    
    def __init__(self: Pipopipette_Gameplay, list_player: list[Player], pipopipette: Pipopipette = Pipopipette()) -> None:
        """
        Args:
            listPlayer: A list of players. Should contain a least two Players
            pipopipette: The playground.
        """
        self.__list_player: Final[list[Player]] = list_player.copy()
        self.__pipopipette: Pipopipette = pipopipette
        self.__current_player_ID: int = self.__list_player[0].ID
        
        for i in range(len(self.__list_player)):
            self.__list_player[i].id = i
            
    # <----- getter ----->
    
    @property
    def list_player(self: Pipopipette_Gameplay) -> list[Player]: return self.__list_player
    
    @property
    def pipopipette(self: Pipopipette_Gameplay) -> Pipopipette: return self.__pipopipette
    
    @property
    def current_player_ID(self: Pipopipette_Gameplay) -> int: return self.__current_player_ID
    
    # <----- setter ----->
    
    @pipopipette.setter
    def pipopipette(self: Pipopipette_Gameplay, pipopipette: Pipopipette) -> None: self.__pipopipette = pipopipette
    
    @current_player_ID.setter
    def current_player_ID(self: Pipopipette_Gameplay, current_player_ID) -> None: self.__current_player_ID = current_player_ID
            
    # <----- nextPlayer ----->
    
    def next_player(self: Pipopipette_Gameplay) -> None:
        """
        Will switch to another player.
        """
        for i in range(len(self.__list_player)):
            if self.__list_player[i].ID == self.current_player_ID: index: int = i + 1
        if index == len(self.__list_player): self.__current_player_ID = self.__list_player[0].ID
        else: self.__current_player_ID = self.__list_player[index].ID
        
        
    # <----- setPlayerTarget ----->
    
    def set_player_target(self: Pipopipette_Gameplay, square_ID: int, side: str) -> bool:
        """
        Used to take a Segment of a square
        Args:
            squareID: The Square to edit
            side: Wich side to manage ? 'l'; 'r', 't', or 'd'.

        Returns:
            Boolean - True if can be taken, False if not
        """
        if self.__pipopipette.valid_target(square_ID, side):
            if self.__pipopipette.set_side(square_ID, side, self.__current_player_ID) != None:
                self.__list_player[self.__current_player_ID].score += 1
                return True
        else: return False
    
    # <----- gameOver ----->
    
    def game_over(self: Pipopipette_Gameplay) -> bool:
        """
        Check if there is a Square without an owner to check if the game ended or not.
        Returns:
            Boolean - True if game finished, False of not

        """
        for square in self.__pipopipette.list_square:
            if square.square_owner == -1: return False
        return True