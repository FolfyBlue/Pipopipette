from jeu.engine.PipopipetteGameplay import PipopipetteGameplay
from random import choice
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
        """Pick a random move for the AI to play

        Args:
            gameplay (PipopipetteGameplay): Game to play on

        Returns:
            tuple[None, None]|tuple[int, str]: Resulting square and side
        """
        moves = PipopipetteAI.__list_moves(gameplay)
        if moves:
            return choice(moves)
        else:
             return (None, None)
    
    @staticmethod
    def move_minmax(gameplay: PipopipetteGameplay, depth: int = 2) -> tuple[None, None]|tuple[int, str]:
        """Pick a move for the AI to play by simulating the next moves

        Args:
            gameplay (PipopipetteGameplay): Game to play on
            depth (int): How many moves to predict forward

        Returns:
            tuple[None, None]|tuple[int, str]: Resulting square and side
        """
        ...