# <========== Import ==========>
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./
    
from jeu.engine.Player.Score import Score

# <========== Tests ==========>

def test_init_getter() -> None:
    """ Test de l'init et du getter
    
    >>> score: Score = Score()
    >>> score.value
    0
    """
    pass

def test_setter() -> None:
    """ Test du setter
    
    >>> score: Score = Score()
    >>> score.value = 5
    >>> score.value 
    5
    """
    pass
    
def test_str() -> None:
    """ Test du __str__
    
    >>> score: Score = Score()
    >>> score.__str__()
    'score is 0.'
    """
    pass
    
def test_comparateur() -> None:
    """ Test des comparateurs
    
    <----- equals ----->
    
    >>> score: Score = Score()
    >>> score2: Score = Score()
    >>> score == score2
    True
    
    >>> score: Score = Score()
    >>> score == 0
    True
    
    >>> score: Score = Score()
    >>> score2: Score = Score(5)
    >>> score == score2
    False
    
    >>> score: Score = Score()
    >>> score == 5
    False
    
    <----- not equals ----->
    
    >>> score: Score = Score()
    >>> score2: Score = Score()
    >>> score != score2
    False
    
    >>> score: Score = Score()
    >>> score != 0
    False
    
    >>> score: Score = Score()
    >>> score2: Score = Score(5)
    >>> score != score2
    True
    
    >>> score: Score = Score()
    >>> score != 5
    True
    
    <----- plus petit que ----->
    
    >>> score: Score = Score()
    >>> score2: Score = Score(5)
    >>> score < score2
    True
    
    >>> score: Score = Score()
    >>> score < 5
    True
    
    >>> score: Score = Score(5)
    >>> score2: Score = Score()
    >>> score < score2
    False
    
    >>> score: Score = Score(5)
    >>> score < 0
    False
    
    <----- plus grand que ----->
    
    >>> score: Score = Score(5)
    >>> score2: Score = Score()
    >>> score > score2
    True
    
    >>> score: Score = Score(5)
    >>> score > 0
    True
    
    >>> score: Score = Score()
    >>> score2: Score = Score(5)
    >>> score > score2
    False
    
    >>> score: Score = Score()
    >>> score > 5
    False
    
    <----- plus petit ou egal que ----->
    
    >>> score: Score = Score()
    >>> score2: Score = Score(5)
    >>> score <= score2
    True
    
    >>> score: Score = Score()
    >>> score <= 5
    True
    
    >>> score: Score = Score(5)
    >>> score2: Score = Score()
    >>> score <= score2
    False
    
    >>> score: Score = Score(5)
    >>> score <= 0
    False
    
    >>> score: Score = Score(5)
    >>> score2: Score = Score(5)
    >>> score <= score2
    True
    
    >>> score: Score = Score(5)
    >>> score <= 5
    True
    
    <----- plus grand ou egal que ----->
    
    >>> score: Score = Score(5)
    >>> score2: Score = Score()
    >>> score >= score2
    True
    
    >>> score: Score = Score(5)
    >>> score >= 0
    True
    
    >>> score: Score = Score()
    >>> score2: Score = Score(5)
    >>> score >= score2
    False
    
    >>> score: Score = Score()
    >>> score >= 5
    False
    
    >>> score: Score = Score(5)
    >>> score2: Score = Score(5)
    >>> score >= score2
    True
    
    >>> score: Score = Score(5)
    >>> score >= 5
    True
    """
    pass

def test_operateur() -> None:
    """ Test des opérateurs
    
    >>> score: Score = Score()
    >>> score = score + 1
    >>> score.value
    1
    
    >>> score: Score = Score()
    >>> score += 1
    >>> score.value
    1
    
    >>> score: Score = Score(1)
    >>> score = score - 1
    >>> score.value
    0
    
    >>> score: Score = Score(1)
    >>> score -= 1
    >>> score.value
    0
    """
    pass

# <========== main ==========>

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)