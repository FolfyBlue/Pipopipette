import pygame
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./

from jeu.ui.popup import Popup
from jeu.utils.font_manager import FontManager
screen: pygame.surface.Surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)
clock: pygame.time.Clock = pygame.time.Clock()
background: pygame.surface.Surface = pygame.image.load("jeu/assets/images/menu_background.png")

textbox_font: FontManager = FontManager("jeu/assets/fonts/Truculenta.ttf")

pygame.init()

popup: Popup = Popup(screen, "Account", (500, 580), "#0575BB")

while True:
    print(int(clock.get_fps()), end=" FPS    \r")
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        popup.update(event)
        match (event.type):
            case pygame.QUIT:
                pygame.quit()
                sys.exit()
            case pygame.MOUSEBUTTONDOWN:
                print("            ", end="\r")  # Clear FPS counter from console
    popup.update_render()

    pygame.display.update()
    clock.tick()