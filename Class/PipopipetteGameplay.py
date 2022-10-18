# <========== Import ==========>

from __future__ import annotations
from Pipopipette import Pipopipette
from Player.Player import Player

# <========== Class ==========>

class PipopipetteGameplay():
    """
    Class used to manage the players, their score, ect...
    """
    
    # <----- init ----->
    
    def __init__(self: PipopipetteGameplay, listPlayer: list[Player], pipopipette: Pipopipette = Pipopipette()) -> None:
        """
        Args:
            listPlayer: A list of players. Should contain a least two Players
            pipopipette: The playground.
        """
        self.__listPlayer: list[Player] = listPlayer.copy()
        self.__pipopipette: Pipopipette = pipopipette
        self.__currentPlayerID: int = 0
        
        for i in range(len(self.__listPlayer)):
            self.__listPlayer[i].id = i
            
    # <----- getter ----->
    
    @property
    def listPlayer(self: PipopipetteGameplay) -> list[Player]: return self.__listPlayer
    
    @property
    def pipopipette(self: PipopipetteGameplay) -> Pipopipette: return self.__pipopipette
    
    @property
    def currentPlayerID(self: PipopipetteGameplay) -> int: return self.__currentPlayerID
    
    # <----- setter ----->
    
    @listPlayer.setter
    def listPlayer(self: PipopipetteGameplay, listPlayer: list[Player]) -> None: self.__listPlayer = listPlayer.copy()
    
    @pipopipette.setter
    def pipopipette(self: PipopipetteGameplay, pipopipette: Pipopipette) -> None: self.__pipopipette = pipopipette
    
    @currentPlayerID.setter
    def currentPlayerID(self: PipopipetteGameplay, currentPlayerID) -> None: self.__currentPlayerID = currentPlayerID
            
    # <----- nextPlayer ----->
    
    def next_player(self: PipopipetteGameplay) -> None:
        """
        Will switch to another player.
        """
        self.__currentPlayerID += 1
        if self.__currentPlayerID % len(self.__listPlayer) == 0: self.__currentPlayerID = 0
        
    # <----- setPlayerTarget ----->
    
    def set_playerTarget(self: PipopipetteGameplay, squareID: int, side: str) -> bool:
        """
        Used to take a Segment of a square
        Args:
            squareID: The Square to edit
            side: Wich side to manage ? 'l'; 'r', 't', or 'd'.

        Returns:
            Boolean - True if can be taken, False if not
        """
        if self.__pipopipette.valid_target(squareID, side): self.__pipopipette.set_side(squareID, side, self.__currentPlayerID); return True
        else: return False
        
    # <----- scoreCount ----->
    
    def score_count(self: PipopipetteGameplay) -> None:
        """
        Update a player score by counting the number of square taken by him.
        """
        for player in self.__listPlayer:
            player.score = 0
            for square in self.__pipopipette.__listSquare:
                if square.squareOwner == player.id: player.score += 1
    
    # <----- gameOver ----->
    
    def game_over(self: PipopipetteGameplay) -> bool:
        """
        Check if there is a Square without an owner to check if the game ended or not.
        Returns:
            Boolean - True if game finished, False of not

        """
        for square in self.__pipopipette.listSquare:
            if square.squareOwner == -1: return False
        return True