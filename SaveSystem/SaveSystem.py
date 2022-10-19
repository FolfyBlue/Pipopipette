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
        with open("../gameData/players.json") as jsonFile:  # Could be an error if used as imported module ?
            jsonObject = json.load(jsonFile)
            jsonFile.close()

        for element in jsonObject:
            if element['username'] == username:
                if bcrypt.checkpw(str.encode(password), str.encode(element['password'])):
                    print("FOUND")
                    raise Exception("We need to implement a Player class to return a Player here")
                    # TODO : Add Player class and create a player here
                else:
                    # User found, but wrong password. We don't need to continue looking for the right user
                    return None
        return None  # Don't found this user

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


if __name__ == '__main__':
    # Unit test
    # print(bcrypt.hashpw(b'1234', bcrypt.gensalt()))
    # print(bcrypt.checkpw(b'1234', b'$2b$12$Fz6ZG4GIm0jRkN35acYaXeoDMPlPQGcclnChced.W.ivZnI5YWv16'))

    SaveSystem.loadPlayer('test', '1234')
