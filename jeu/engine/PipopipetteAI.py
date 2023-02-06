from jeu.engine.PipopipetteGameplay import PipopipetteGameplay
from random import randint, choice
class PipopipetteAI:
    """Class which will be used to control the AI's logic.
    """
    @staticmethod
    def move(gameplay: PipopipetteGameplay, player: int) -> tuple[int, str]:
        move_square: int = -1
        move_side: str = ''
        while not gameplay.pipopipette.valid_target(move_square, move_side):
            move_square = randint(0, len(gameplay.pipopipette.list_square))
            move_side = choice(('l','r','t','d'))
        # gameplay.set_player_target(move_square, move_side)
        # if move_side in ('t', 'd'):
        #     j: int = move_square//gameplay.pipopipette.WIDTH
        #     i: int = move_square%gameplay.pipopipette.WIDTH
        # else:
        #     j: int = move_square//gameplay.pipopipette.WIDTH
        #     i: int = move_square%gameplay.pipopipette.WIDTH
        #     if move_side == 'r' and i == gameplay.pipopipette.WIDTH-1:
        #         i += 1
        return move_square, move_side