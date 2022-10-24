from jeu.engine.Player.Player import Player

import json
import bcrypt

SAVE_FILE_PATH = "../gameData/players.json"

class SaveSystem():
    """
    Static Class used to save and load data. Will not update the password for this player
    """

    def __init__(self):
        raise Exception("This is a static class !")

    @staticmethod
    def save_player(player: Player) -> None:
        """
        Save a player object in storage. Will not update the password for this player
        Args:
            player: The Player to save
        """
        with open(SAVE_FILE_PATH) as json_file:  # File loaded
            json_object = json.load(json_file)
            json_file.close()

        for i in range(len(json_object)):  # Loop to get the right entry for this user
            if json_object[i]['username'] == player.NAME:
                # if bcrypt.checkpw(str.encode(player.getPassword()), str.encode(jsonObject[i]['password'])):
                # Found user to edit
                new_entry = {}  # I create a new entry that will replace the old one
                new_entry['username'] = player.NAME
                new_entry['password'] = json_object[i]['password']
                new_entry['id'] = player.ID
                new_entry['points'] = player.score.value

                json_object[i] = new_entry  # Old entry replaced

        with open(SAVE_FILE_PATH, "w") as file:  # The new file with data is written
            json.dump(json_object, file)
            file.close()

    @staticmethod
    def load_player(username: str, password: str) -> Player | None:
        """
        Get the saved data of someone, with his username and password
        Args:
            username: The username of this user
            password: The password of this user

        Returns: Player if found someone with this username and password, None if something went wrong

        """
        with open(SAVE_FILE_PATH) as json_file:
            json_object = json.load(json_file)
            json_file.close()

        for element in json_object:
            if element['username'] == username:
                if bcrypt.checkpw(str.encode(password), str.encode(element['password'])):
                    return Player(username, element['id'], element['points'])
                else:
                    # User found, but wrong password. We don't need to continue looking for the right user
                    return None
        return None  # Don't found this user

    @staticmethod
    def create_user(username: str, password: str, id: int, points: int = 0) -> Player:
        """
        Register a new user in the save system
        Args:
            username: The username of this user
            password: A password
            id: An unique ID for this user
            points: The number of points for this player

        Returns: A Player object
        """
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


if __name__ == '__main__':
    # Unit test
    print(bcrypt.hashpw(b'1234', bcrypt.gensalt()))
    print(bcrypt.checkpw(b'1234', b'$2b$12$Fz6ZG4GIm0jRkN35acYaXeoDMPlPQGcclnChced.W.ivZnI5YWv16'))

    player: Player = SaveSystem.load_player('test', '1234')
    print(player)
    SaveSystem.save_player(player)
    #SaveSystem.create_user("TEST1234", "9876", 7326576, 8)