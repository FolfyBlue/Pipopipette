# <========== import ==========>
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./
    
from Class.Player.Player import Player
from Class.Player.Score import Score

# <========== test ==========>

def test_init_getter() -> None:
    """ test de l'init et des getter
    
    >>> player: Player = Player('player',1)
    >>> player.NAME
    'player'
    
    >>> player: Player = Player('player',1)
    >>> player.ID
    1
    
    >>> player: Player = Player('player',1)
    >>> type(player.score)
    <class 'Class.Player.Score.Score'>
    """
    pass

def test_setter() -> None:
    """ test du setter
    
    >>> player: Player = Player('player',1)
    >>> player.score += 1
    >>> player.score.value
    1
    """
    pass

def test_str() -> None:
    """ test de __str__
    
    >>> player: Player = Player('player',1)
    >>> player.__str__()
    'player score is 0.'
    """
    
# <========== main ==========>

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)