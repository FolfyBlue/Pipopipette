# <========== import ==========>
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./
    
from Class.Square.Square import Square
from Class.Square.Segment import Segment

# <========== test ==========>

def test_init_getter() -> None:
    """ test de l'init et des getter
    
    >>> square: Square = Square()
    >>> square.ID
    0
    
    >>> square: Square = Square()
    >>> square.square_owner
    -1
    
    >>> square: Square = Square()
    >>> type(square.left)
    <class 'Class.Square.Segment.Segment'>
    
    >>> square: Square = Square()
    >>> type(square.right)
    <class 'Class.Square.Segment.Segment'>
    
    >>> square: Square = Square()
    >>> type(square.top)
    <class 'Class.Square.Segment.Segment'>
    
    >>> square: Square = Square()
    >>> type(square.down)
    <class 'Class.Square.Segment.Segment'>
    """
    pass
    
def test_setter() -> None:
    """ test des setter
    
    >>> square: Square = Square()
    >>> square.left = 1
    >>> square.left.owner_ID
    1
    
    >>> square: Square = Square()
    >>> square.right = 1
    >>> square.right.owner_ID
    1
    
    >>> square: Square = Square()
    >>> square.top = 1
    >>> square.top.owner_ID
    1
    
    >>> square: Square = Square()
    >>> square.down = 1
    >>> square.down.owner_ID
    1
    
    >>> square: Square = Square()
    >>> square.square_owner = 1
    >>> square.square_owner
    1
    
    >>> square: Square = Square()
    >>> square.left = 1
    >>> square.right = 1
    >>> square.top = 1
    >>> square.down = 1
    >>> square.square_owner
    1
    """
    pass

# <========== main ==========>

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)