import pygame
import sys, os

parentdir = os.path.realpath(os.path.join(os.path.dirname(__file__),os.pardir))
if parentdir not in sys.path:
    sys.path.insert(1, parentdir) # insert ../ just after ./

from jeu.ui.checkbox import Checkbox
from jeu.utils.font_manager import FontManager
screen: pygame.surface.Surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)
clock: pygame.time.Clock = pygame.time.Clock()
background: pygame.surface.Surface = pygame.image.load("jeu/assets/images/menu_background.png")

checkbox_font: FontManager = FontManager("jeu/assets/fonts/Truculenta.ttf")

pygame.init()

checkbox: Checkbox = Checkbox(
    screen=screen,
    position=(150,150),
    checked_image=pygame.image.load("jeu/assets/images/checkbox_checked.png"),
    unchecked_image=pygame.image.load("jeu/assets/images/checkbox_unchecked.png"),
    text="Checkbox",
    font=checkbox_font.get_font(75),
    color="white",
    on_check=lambda: print("Checked!"),
    on_uncheck=lambda: print("Unchecked!"),
)


checkbox2: Checkbox = Checkbox(
    screen=screen,
    position=(300,300),
    checked_image=pygame.image.load("jeu/assets/images/checkbox_checked.png"),
    unchecked_image=pygame.image.load("jeu/assets/images/checkbox_unchecked.png"),
    text="Checkbox two",
    font=checkbox_font.get_font(25),
    color="black",
    text_offset= -25,
    on_check=lambda: print("Checked 2!"),
    on_uncheck=lambda: print("Unchecked 2!"),
    checked=True
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
        checkbox.update(event)
        checkbox2.update(event)
    checkbox.update_render()
    checkbox2.update_render()

    pygame.display.update()
    clock.tick()