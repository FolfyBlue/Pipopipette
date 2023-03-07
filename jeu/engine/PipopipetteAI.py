from jeu.engine.PipopipetteGameplay import PipopipetteGameplay
from random import randint, choice
class PipopipetteAI:
    """Class which will be used to control the AI's logic.
    """

    @staticmethod
    def __list_moves(gameplay: PipopipetteGameplay) -> list[tuple[int, str]]:
        results: list[tuple[int, str]] = []
        for square in gameplay.pipopipette.list_square:
            if square.square_owner == -1:
                if square.left.owner_ID == -1:
                    results.append((square.ID, 'l'))
                if square.top.owner_ID == -1:
                        results.append((square.ID, 't'))
                if square.right.owner_ID == -1:
                        results.append((square.ID, 'r'))
                if square.down.owner_ID == -1:
                        results.append((square.ID, 'd'))
        return results


    @staticmethod
    def move_random(gameplay: PipopipetteGameplay) -> tuple[None, None]|tuple[int, str]:
        moves = PipopipetteAI.__list_moves(gameplay)
        if moves:
            return choice(moves)
        else:
             return (None, None)