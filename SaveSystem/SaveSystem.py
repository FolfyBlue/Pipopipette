import json
from pathlib import Path

import bcrypt
from time import time

from jeu.engine.Player.Player import Player

SAVE_FOLDER_PATH = str(Path.home()) + "/Pipopipette"
SAVE_FILE_PATH = SAVE_FOLDER_PATH + "/players.json"

class SaveSystem():
    """
    Static Class used to save and load data
    """

    def __init__(self):
        raise Exception("This is a static class !")

    @staticmethod
    def save_player(player: Player) -> None:
        """Save a player object in storage. Will not update the password for this player

        Args:
            player (Player): Player to save.
        """
        SaveSystem.__ensure_exists()
        with open(SAVE_FILE_PATH) as json_file:  # File loaded
            json_object = json.load(json_file)
            json_file.close()

        for i in range(len(jsonObject)):  # Loop to get the right entry for this user
            if jsonObject[i]['username'] == player.NAME:
                # if bcrypt.checkpw(str.encode(player.getPassword()), str.encode(jsonObject[i]['password'])):
                # Found user to edit
                newEntry = {}  # I create a new entry that will replace the old one
                newEntry['username'] = player.NAME
                newEntry['password'] = jsonObject[i]['password']
                newEntry['id'] = player.ID
                newEntry['points'] = player.score.value

                jsonObject[i] = newEntry  # Old entry replaced

        with open(SAVE_FILE_PATH, "w") as file:  # The new file with data is written
            json.dump(jsonObject, file)
            file.close()

    @staticmethod
    def load_player(username: str, password: str) -> Player | None:
        """Get the saved data of someone, with his username and password

        Args:
            username (str): The username of this user
            password (str): The password of this user

        Returns:
            Player | None: Player if found someone with this username and password, None if something went wrong
        """
        SaveSystem.__ensure_exists()
        with open(SAVE_FILE_PATH) as json_file:
            json_object = json.load(json_file)
            json_file.close()

        for element in json_object:
            if element['username'] == username:
                if bcrypt.checkpw(str.encode(password), str.encode(element['password'])):
                    return Player(username, element['id'], element['points'])
                else:
                    # User found, but wrong password. We don't need to continue looking for the right user
                    print("Wrong password !")
                    return None
        return None  # Don't found this user

    @staticmethod
    def is_login_already_taken(username: str) -> bool:
        """
        Check if a login is still available

        Args:
            username (str): The username of this user

        Returns:
            bool: True of False. False = Login can be registered
        """
        SaveSystem.__ensure_exists()
        with open(SAVE_FILE_PATH) as json_file:
            json_object = json.load(json_file)
            json_file.close()

        taken = False

        for element in json_object:
            if element['username'] == username:
                taken = True
        return taken  # Don't found this username

    @staticmethod
    def create_user(username: str, password: str, id: int, points: int = 0) -> Player|None:
        """Register a new user in the save system

        Args:
            username (str): The username of this user
            password (str): The password of this user
            id (int): The unique identifier of the user
            points (int, optional): The number of points this player has. Defaults to 0.

        Returns:
            Player|None: A player object, or None if it couldn't be created.
        """
        if (not username) or (not password) or (SaveSystem.is_login_already_taken(username)):
            return None
        SaveSystem.__ensure_exists()
        with open(SAVE_FILE_PATH) as json_file:
            json_object = json.load(json_file)
            json_file.close()

        new_entry = {
            'username': username,
            'password': bcrypt.hashpw(str.encode(password), bcrypt.gensalt()).decode("utf-8"),
            'id': id,
            'points': points
        }

        json_object.append(new_entry)

        with open(SAVE_FILE_PATH, "w") as file:
            json.dump(json_object, file)
            file.close()

        return Player(username, id, points)

    @staticmethod
    def get_first_available_ID() -> int:
        """Method used to get the first available ID in the local account database

        Returns:
            int: Available ID
        """
        SaveSystem.__ensure_exists()
        with open(SAVE_FILE_PATH) as json_file:
            json_object = json.load(json_file)
            json_file.close()

        idAvailable = 0

        for player in json_object:
            if int(player["id"]) > idAvailable: idAvailable = int(player["id"])

        return int(idAvailable) + 1
    
    @staticmethod
    def __ensure_exists():
        """Ensures the save folder path and file exists, and are not corrupted.
        """
        # Create the folder
        Path(SAVE_FOLDER_PATH).mkdir(parents=True, exist_ok=True)
        # Create the save file if it doesn't exist
        if not Path(SAVE_FILE_PATH).is_file():
            with open(SAVE_FILE_PATH, 'w') as f:
                f.write("[]")

        # Try and read the save file to see if it's corrupted,
        # if it is, make a backup of the old one and create a new one 
        with open(SAVE_FILE_PATH) as json_file:
            try:
                json.load(json_file)
            except json.JSONDecodeError:
                print("The players file is corrupted! Creating a new one..")
                corrupted_file = Path(SAVE_FOLDER_PATH)
                corrupted_file.rename(Path(SAVE_FOLDER_PATH+f"/{time()}.json"))
                with open(SAVE_FILE_PATH, 'w') as f:
                    f.write("[]")


if __name__ == '__main__':
    # Unit test
    print(bcrypt.hashpw(b'1234', bcrypt.gensalt()))
    print(bcrypt.checkpw(b'1234', b'$2b$12$Fz6ZG4GIm0jRkN35acYaXeoDMPlPQGcclnChced.W.ivZnI5YWv16'))

    player: Player|None = SaveSystem.load_player('test', '1234')
    print(player)
    if isinstance(player, Player):
        SaveSystem.save_player(player)
    # SaveSystem.create_user("TEST1234", "9876", 7326576, 8)
