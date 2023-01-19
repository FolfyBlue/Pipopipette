import pygame
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./

from jeu.ui.checkbox import Checkbox
from jeu.ui.button import Button
from jeu.ui.ui import UI
from jeu.ui.textbox import Textbox
from jeu.ui.popup import Popup
from jeu.utils.font_manager import FontManager
screen: pygame.surface.Surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)
clock: pygame.time.Clock = pygame.time.Clock()
background: pygame.surface.Surface = pygame.image.load("jeu/assets/images/menu_background.png")

font: FontManager = FontManager("jeu/assets/fonts/Truculenta.ttf")

pygame.init()

checkbox: Checkbox = Checkbox(
    screen=screen,
    position=(150,150),
    checked_image=pygame.image.load("jeu/assets/images/checkbox_checked.png"),
    unchecked_image=pygame.image.load("jeu/assets/images/checkbox_unchecked.png"),
    text="Checkbox",
    font=font.get_font(75),
    color="white",
    on_check=lambda: print("Checked!"),
    on_uncheck=lambda: print("Unchecked!"),
)

button = Button(
    screen=screen,
    image=pygame.image.load("jeu/assets/images/Play Rect.png"),
    position=(1280-350, 150),
    text="Button",
    font=font.get_font(75),
    color="#FFFFFF",
    hover_color="#d7fcd4",
    action=lambda: ...
)

textbox: Textbox = Textbox(
    screen,
    (640, 500),
    "Textbox",
    font.get_font(50),
    (250, 75)
)

popup: Popup = Popup(screen, "Popup", (300, 150), "#0575BB")

elements: list[UI] = [button, checkbox, textbox]

while True:
    print(int(clock.get_fps()), end=" FPS    \r")
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        match (event.type):
            case pygame.QUIT:
                quit()
            case pygame.MOUSEBUTTONDOWN:
                print("            ", end="\r")  # Clear FPS counter from console
        for element in elements:
            element.update(event)
    for element in elements:
        element.update_render()
    popup.run()
    pygame.display.update()
    clock.tick()