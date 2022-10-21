# <========== import ==========>
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./
    
from Class.Player.Player import Player
from Class.Pipopipette import Pipopipette
from Class.PipopipetteGameplay import PipopipetteGameplay

# <========== test ==========>

def test_init_getter() -> None:
    """ test de l'init et des getter
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> type(pipoG.LIST_PLAYER[0])
    <class 'Class.Player.Player.Player'>
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> pipoG.LIST_PLAYER[0].NAME
    'player_name'
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> type(pipoG.pipopipette)
    <class 'Class.Pipopipette.Pipopipette'>
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> pipoG.current_player_ID
    0
    """
    pass

def test_setter() -> None:
    """ test du setter
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> pipoG.current_player_ID = 1
    >>> pipoG.current_player_ID
    1
    """
    pass

def test_next_player() -> None:
    """ test de next_player
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name","player_name_2"])
    >>> pipoG.next_player()
    >>> pipoG.current_player_ID
    1
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> pipoG.next_player()
    >>> pipoG.next_player()
    >>> pipoG.current_player_ID
    0
    """
    pass

def test_set_player_target() -> None:
    """ test de set_player_target()
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> pipoG.set_player_target(0,'l')
    >>> pipoG.pipopipette.get_square_by_ID(0).left.owner_ID
    0
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> pipoG.set_player_target(1,"r")
    >>> pipoG.set_player_target(1,"l")
    >>> pipoG.set_player_target(1,"t")
    >>> pipoG.set_player_target(1,"d")
    >>> pipoG.LIST_PLAYER[pipoG.current_player_ID].score.value
    1
    """
    pass

def test_game_over() -> None:
    """ test de game_over
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"], Pipopipette(1,1))
    >>> pipoG.set_player_target(0,'l')
    >>> pipoG.set_player_target(0,'r')
    >>> pipoG.set_player_target(0,'t')
    >>> pipoG.set_player_target(0,'d')
    >>> pipoG.game_over()
    True
    
    >>> pipoG: PipopipetteGameplay = PipopipetteGameplay(["player_name"])
    >>> pipoG.set_player_target(0,'l')
    >>> pipoG.set_player_target(0,'r')
    >>> pipoG.set_player_target(0,'t')
    >>> pipoG.set_player_target(0,'d')
    >>> pipoG.game_over()
    False
    """
    pass
# <========== main ==========>

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)