# <========== import ==========>
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./
    
from jeu.engine.Square.Segment import Segment

# <========== test ==========>

def test_init_getter() -> None:
    """ test de l'init et du getter
    
    >>> segment: Segment = Segment()
    >>> segment.owner_ID
    -1
    """
    pass
    
def test_setter() -> None:
    """ test du setter
    
    >>> segment: Segment = Segment()
    >>> segment.owner_ID = 1
    >>> segment.owner_ID
    1
    """
    pass

# <========== main ==========>

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)