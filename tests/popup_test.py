import pygame
import sys
import os

parentdir = os.path.realpath(os.path.join(
    os.path.dirname(__file__), os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir)  # insert ../ just after ./

from jeu.utils.font_manager import FontManager
from jeu.ui.popup import Popup
from jeu.ui.textbox import Textbox

screen: pygame.surface.Surface = pygame.display.set_mode(
    (1280, 720), pygame.RESIZABLE | pygame.SCALED)
clock: pygame.time.Clock = pygame.time.Clock()
background: pygame.surface.Surface = pygame.image.load(
    "jeu/assets/images/menu_background.png")

textbox_font: FontManager = FontManager("jeu/assets/fonts/Truculenta.ttf")

pygame.init()

popup: Popup = Popup(screen, "Account", (500, 580), "#0575BB")
textbox: Textbox = Textbox(
    popup.surface,
    (200, 240),
    "Placeholder",
    textbox_font.get_font(50),
    (250, 75)
)

popup.add_ui_element(textbox)

screen.blit(background, (0, 0))
pygame.display.update()

popup.run()

pygame.quit()
sys.exit()