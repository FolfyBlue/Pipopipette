import pygame
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./

from jeu.ui.textbox import Textbox
from jeu.utils.font_manager import FontManager
screen: pygame.surface.Surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)
clock: pygame.time.Clock = pygame.time.Clock()
background: pygame.surface.Surface = pygame.image.load("jeu/assets/images/menu_background.png")

textbox_font: FontManager = FontManager("jeu/assets/fonts/Truculenta.ttf")

pygame.init()

textbox: Textbox = Textbox(
    screen,
    (640, 500),
    "Placeholder",
    textbox_font.get_font(50),
    (250, 75)
)

while True:
    print(int(clock.get_fps()), end=" FPS    \r")
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        match (event.type):
            case pygame.QUIT:
                quit()
            case pygame.MOUSEBUTTONDOWN:
                print("            ", end="\r")  # Clear FPS counter from console
        textbox.update(event)
    textbox.update_render()

    pygame.display.update()
    clock.tick()