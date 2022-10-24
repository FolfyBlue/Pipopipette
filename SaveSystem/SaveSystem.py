import json
import bcrypt

SAVE_FILE_PATH = "../gameData/players.json"
class Player():  # TODO : Used just to avoid errors on compilation. Delete this when the real Plater class is ready !
    def get_username(self):
        pass

    def get_password(self):
        pass

    def get_id(self):
        pass

    def get_points(self):
        pass

class SaveSystem():
    """
    Static Class used to save and load data
    """

    def __init__(self):
        raise Exception("This is a static class !")

    @staticmethod
    def save_player(player: Player) -> None:
        """
        Save a player object in storage
        Args:
            player: The Player to save
        """
        with open(SAVE_FILE_PATH) as json_file:  # File loaded
            json_object = json.load(json_file)
            json_file.close()

        new_entry = {}  # I create a new entry that will replace the old one
        new_entry['username'] = "Replace me"  # TODO
        new_entry['password'] = "1234"  # TODO : get password and hash it
        new_entry['id'] = "987123"
        new_entry['points'] = 20

        for i in range(len(json_object)):  # Loop to get the right entry for this user
            if json_object[i]['username'] == player.get_username():
                if bcrypt.checkpw(str.encode(player.get_password()), str.encode(json_object[i]['password'])):
                    # Found user to edit
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
                    print("FOUND")
                    raise NotImplementedError("We need to implement a Player class to return a Player here")
                    # TODO : Add Player class and create a player here
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

        # TODO : add Player return


if __name__ == '__main__':
    # Unit test
    # print(bcrypt.hashpw(b'1234', bcrypt.gensalt()))
    # print(bcrypt.checkpw(b'1234', b'$2b$12$Fz6ZG4GIm0jRkN35acYaXeoDMPlPQGcclnChced.W.ivZnI5YWv16'))

    #SaveSystem.loadPlayer('test', '1234')
    # SaveSystem.savePlayer(None)
    SaveSystem.create_user("TEST1234", "9876", 7326576, 8)
