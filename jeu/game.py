import time

import pygame

from jeu.engine.Pipopipette import Pipopipette
from jeu.engine.PipopipetteGameplay import PipopipetteGameplay
from jeu.ui.button import Button
from jeu.ui.ui import UI
from jeu.utils.assets_import import resource_path
from jeu.utils.font_manager import FontManager

LINE_WIDTH = 9
HEIGHT_OFFSET = 250
WIDTH_OFFSET = 200
PLAYER1_COLOR = "blue"
PLAYER2_COLOR = "red"
PLAYER_COLORS = (PLAYER1_COLOR, PLAYER2_COLOR)
PLAYER_COUNT = 2


def formatted_score(score: int) -> str:
    return f"{score:03d}"


def formatted_time(time_in_seconds: int) -> str:
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def get_timer_label(start_time_in_seconds: float, font: FontManager):
    time_elapsed_in_seconds = int(time.time() - start_time_in_seconds)
    timer_label: pygame.surface.Surface = font.get_font(75).render(
        formatted_time(time_elapsed_in_seconds), True, "#EEEEEE")
    timer_rect: pygame.rect.Rect = timer_label.get_rect(center=(640, 50))
    return (timer_label, timer_rect)


def get_score_label(score: int, font: FontManager, player1: bool):
    if player1:
        xpos: int = 100
        color: str = PLAYER1_COLOR
    else:
        xpos: int = 1280-100
        color: str = PLAYER2_COLOR
    player_score_label: pygame.surface.Surface = font.get_font(
        75).render(f"{score:03d}", True, color)
    player_score_rect: pygame.rect.Rect = player_score_label.get_rect(
        center=(xpos, 650))
    return (player_score_label, player_score_rect)


def game(screen: pygame.surface.Surface, size: tuple[int, int] = (10, 5), players: tuple[str, str]=("Playername00", "Playername01")):
    """Game screen

    Args:
        screen (pygame.surface.Surface): Screen to display the game on
        size (tuple[int, int]): Size of the grid to play on
        players (tuple[str, str]): List of usernames for the players
    """

    pipo: Pipopipette = Pipopipette(*size)
    gameplay: PipopipetteGameplay = PipopipetteGameplay(list_player_name=list(players), pipopipette=pipo)

    clock: pygame.time.Clock = pygame.time.Clock()
    pygame.display.set_caption("Pipopipette")

    game_font: FontManager = FontManager(
        resource_path("jeu/assets/fonts/Truculenta.ttf"))

    background: pygame.surface.Surface = pygame.image.load(
        resource_path("jeu/assets/images/game_background.png"))

    labels: dict[str, tuple[pygame.surface.Surface, pygame.rect.Rect]] = {}
    start_time_in_seconds: float = time.time()

    player1_label: pygame.surface.Surface = game_font.get_font(
        33).render("Playername01", True, "#EEEEEE")
    player1_rect: pygame.rect.Rect = player1_label.get_rect(center=(100, 593))
    player2_label: pygame.surface.Surface = game_font.get_font(
        33).render("Playername02", True, "#EEEEEE")
    player2_rect: pygame.rect.Rect = player2_label.get_rect(
        center=(1280-100, 593))

    labels["timer"] = get_timer_label(time.time(), game_font)
    labels["player1"] = (player1_label, player1_rect)
    labels["player2"] = (player2_label, player2_rect)
    labels["player1_score"] = get_score_label(0, game_font, True)
    labels["player2_score"] = get_score_label(0, game_font, False)

    started = False

    grid_height = 1280-WIDTH_OFFSET
    grid_width = 720-HEIGHT_OFFSET
    segments_height = grid_height//size[0]
    segments_width = grid_width//size[1]

    board_elements: list[UI] = []
    fillers: list[pygame.Rect] = []
    owned_segments: dict[tuple[int, int, str], int] = {}

    def segment_handler(square_id: int, side: str, i: int, j: int):
        print(square_id, side, i, j)
        nonlocal owned_segments
        if gameplay.pipopipette.valid_target(square_id, side):
            gameplay.set_player_target(square_id, side)
            owned_segments[(i, j, side)] = gameplay.current_player_ID
            gameplay.next_player()
        else:
            print(square_id, side, (i, j), "is not a valid target!")

    def update_board():
        board_elements: list[UI] = []
        fillers: list[pygame.Rect] = []
        for i in range(size[0]+1):
            for j in range(size[1]+1):
                x_position: int = segments_height*i+HEIGHT_OFFSET//1.75-22  # type: ignore
                y_position: int = segments_width*j+WIDTH_OFFSET//1.75  # type: ignore
                filler = pygame.Rect(x_position, y_position,
                                     LINE_WIDTH, LINE_WIDTH)
                filler.center = (x_position-LINE_WIDTH*2.3,  # type: ignore
                                 y_position-LINE_WIDTH*2.3)
                fillers.append(filler)

                if i != size[0]:
                    if (i, j, 't') in owned_segments:
                        color: str = PLAYER_COLORS[owned_segments[(i, j,'t')]]
                    elif (i, j, 'd') in owned_segments:
                        color: str = PLAYER_COLORS[owned_segments[(i, j,'d')]]
                    else:
                        color: str = "white"
                    def vertical_segment_handler(i: int, j: int):
                        square_id = i+size[0]*j
                        side: str = 't'
                        if square_id > len(pipo.list_square)-1:
                            side = 'd'
                            square_id = square_id-size[0]

                        segment_handler(square_id, side, i, j)         

                    x_segment: Button = Button(
                        screen=screen,
                        image=pygame.image.load(resource_path(
                            f"jeu/assets/images/{color}.png")),
                        position=(x_position+LINE_WIDTH, y_position),
                        text="",
                        font=game_font.get_font(10),
                        color="WHITE",
                        hover_color="BLACK",
                        action=lambda i=i, j=j: vertical_segment_handler(i, j),
                        enforced_size=(segments_height-LINE_WIDTH, LINE_WIDTH)
                    )
                    board_elements.append(x_segment)
                if j != size[1]:
                    if (i, j, 'l') in owned_segments:
                        color: str = PLAYER_COLORS[owned_segments[(i, j,'l')]]
                    elif (i, j, 'r') in owned_segments:
                        color: str = PLAYER_COLORS[owned_segments[(i, j,'r')]]
                    else:
                        color: str = "white"
                    def horizontal_segment_handler(i: int, j: int):
                        newi: int = i-(i//size[0])
                        side: str = 'l'
                        if i % size[0] == 0 and i != newi:
                            side = "r"
                        square_id = newi+size[0]*j

                        segment_handler(square_id, side, i, j)
                        
                    y_segment: Button = Button(
                        screen=screen,
                        image=pygame.image.load(resource_path(
                            f"jeu/assets/images/{color}.png")),
                        position=(x_position, y_position+LINE_WIDTH),
                        text="",
                        font=game_font.get_font(10),
                        color="WHITE",
                        hover_color="BLACK",
                        action=lambda i=i, j=j: horizontal_segment_handler(i, j),
                        enforced_size=(LINE_WIDTH, segments_width-LINE_WIDTH)
                    )
                    board_elements.append(y_segment)
        return board_elements, fillers

    board_elements, fillers = update_board()
    while True:
        if started:

            board_elements, fillers = update_board()
            labels["timer"] = get_timer_label(start_time_in_seconds, game_font)
            score: list[int] = gameplay.get_score()
            labels["player1_score"] = get_score_label(score[0], game_font, True)
            labels["player2_score"] = get_score_label(score[1], game_font, False)
        print(int(clock.get_fps()), end=" FPS    \r")
        screen.blit(background, (0, 0))
        for surface, rect in labels.values():
            screen.blit(surface, rect)

        for event in pygame.event.get():
            for element in board_elements:
                element.update(event)
            match (event.type):
                case pygame.QUIT:
                    quit()
                case pygame.MOUSEBUTTONDOWN:
                    if not started:
                        started = True
                        start_time_in_seconds = time.time()
                    # Clear FPS counter from console
                    print("            ", end="\r")
        for filler in fillers:
            pygame.draw.rect(screen, "#EEEEEE", filler)
        for element in board_elements:
            element.update_render()
        pygame.display.update()
        clock.tick()
