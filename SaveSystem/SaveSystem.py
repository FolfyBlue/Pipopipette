class Player():  # Used just to avoid errors on compilation. Delete this when the real Plater class is ready !
    pass

import json
import bcrypt


class SaveSystem():
    """
    Static Class used to save and load data
    """

    def __init__(self):
        raise Exception("This is a static class !")

    @staticmethod
    def savePlayer(player: Player) -> None:
        """
        Save a player object in storage
        Args:
            player: The Player to save
        """
        pass

    @staticmethod
    def loadPlayer(username: str, password: str) -> Player | None:
        """
        Get the saved data of someone, with his username and password
        Args:
            username: The username of this user
            password: The password of this user

        Returns: Player if found someone with this username and password, None if something went wrong

        """
        pass

    @staticmethod
    def createNewUser(username: str, password: str, id: int, points: int = 0) -> Player:
        """
        Register a new user in the save system
        Args:
            username: The username of this user
            password: A password
            id: An unique ID for this user
            points: The number of points for this player

        Returns: A Player object
        """
        pass
