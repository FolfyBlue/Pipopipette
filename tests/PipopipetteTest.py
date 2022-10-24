# <========== import ==========>
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./
    
from jeu.engine.Square.Square import Square
from jeu.engine.Pipopipette import Pipopipette

# <========== test ==========>

def test_init_getter() -> None:
    """ test de l'init et des getter
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.WIDTH
    5
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.HEIGHT
    5
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> type(pipo.list_square)
    <class 'list'>
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> len(pipo.list_square)
    25
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> type(pipo.list_square[0])
    <class 'jeu.engine.Square.Square.Square'>
    """
    pass

def test_setter() -> None:
    """ test du setter
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.list_square = [Square(1)]
    >>> pipo.list_square[0].ID
    1
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.list_square = [Square(1)]
    >>> len(pipo.list_square)
    1
    """
    pass

def test_get_square_by_ID() -> None:
    """ test de get_square_by_ID
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.get_square_by_ID(1).ID
    1
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.get_square_by_ID(100) is None
    True
    """
    pass

def test_set_side() -> None:
    """ test de set_side
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.set_side(0,'l',1)
    >>> pipo.get_square_by_ID(0).left.owner_ID
    1
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.set_side(0,'r',1)
    >>> pipo.get_square_by_ID(0).right.owner_ID
    1
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.set_side(0,'t',1)
    >>> pipo.get_square_by_ID(0).top.owner_ID
    1
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.set_side(0,'d',1)
    >>> pipo.get_square_by_ID(0).down.owner_ID
    1
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.set_side(0,'l',1)
    >>> pipo.set_side(0,'r',1)
    >>> pipo.set_side(0,'t',1)
    >>> pipo.set_side(0,'d',1)
    >>> pipo.get_square_by_ID(0).square_owner
    1
    """
    pass

def test_valid_target() -> None:
    """ test de valid_target:
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.valid_target(0,'l')
    True
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.set_side(0,'l',1)
    >>> pipo.valid_target(0,'l')
    False
    
    >>> pipo: Pipopipette = Pipopipette()
    >>> pipo.valid_target(100,'l')
    False
    """

# <========== main ==========>

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    