# <========== Import ==========>

from __future__ import annotations
from typing import Final
from Pipopipette import Pipopipette
from Player.Player import Player

# <========== Class ==========>

class PipopipetteGameplay():
    """
    Class used to manage the players, their score, ect...
    """
    
    # <----- init ----->
    
    def __init__(self: PipopipetteGameplay, list_player_name: list[str], pipopipette: Pipopipette = Pipopipette()) -> None:
        """
        Args:
            listPlayer: A list of players. Should contain a least two Players
            pipopipette: The playground.
        """
        self.__list_player: Final[list[Player]] = [Player(list_player_name[i],i) for i in range(len(list_player_name))]
        self.__pipopipette: Pipopipette = pipopipette
        self.__current_player_ID: int = self.__list_player[0].ID
            
    # <----- getter ----->
    
    @property
    def list_player(self: PipopipetteGameplay) -> list[Player]: return self.__list_player
    
    @property
    def pipopipette(self: PipopipetteGameplay) -> Pipopipette: return self.__pipopipette
    
    @property
    def current_player_ID(self: PipopipetteGameplay) -> int: return self.__current_player_ID
    
    # <----- setter ----->
    
    @pipopipette.setter
    def pipopipette(self: PipopipetteGameplay, pipopipette: Pipopipette) -> None: self.__pipopipette = pipopipette
    
    @current_player_ID.setter
    def current_player_ID(self: PipopipetteGameplay, current_player_ID) -> None: self.__current_player_ID = current_player_ID
            
    # <----- nextPlayer ----->
    
    def next_player(self: PipopipetteGameplay) -> None:
        """
        Will switch to another player.
        """
        self.__currentPlayerID += 1
        if self.__currentPlayerID % len(self.__listPlayer) == 0: self.__currentPlayerID = 0
        
        
    # <----- setPlayerTarget ----->
    
    def set_player_target(self: PipopipetteGameplay, square_ID: int, side: str) -> bool:
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
    
    def game_over(self: PipopipetteGameplay) -> bool:
        """
        Check if there is a Square without an owner to check if the game ended or not.
        Returns:
            Boolean - True if game finished, False of not

        """
        for square in self.__pipopipette.list_square:
            if square.square_owner == -1: return False
        return True