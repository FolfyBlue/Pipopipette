from jeu.engine.PipopipetteGameplay import PipopipetteGameplay
from random import randint, choice
class PipopipetteAI:
    """Class which will be used to control the AI's logic.
    """
    @staticmethod
    def move_random(gameplay: PipopipetteGameplay) -> tuple[int, str]:
        move_square: int = -1
        move_side: str = ''
        while not gameplay.pipopipette.valid_target(move_square, move_side):
            move_square = randint(0, len(gameplay.pipopipette.list_square))
            move_side = choice(('l','r','t','d'))

        return move_square, move_side