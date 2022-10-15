import sys

import pygame
from jeu.ui.button import Button
from jeu.ui.popup import Popup
from jeu.ui.textbox import Textbox
from jeu.ui.ui import UI
from jeu.utils.font_manager import FontManager


def close_login_screen():
    global active
    active = False


def login_handler():
    print("Login!")
    close_login_screen()


def register_handler():
    print("Register!")
    close_login_screen()


def login_screen(screen: pygame.surface.Surface):
    """Login screen

    Args:
        screen (pygame.surface.Surface): Screen to display the menu on
    """
    global active
    active = True
    clock: pygame.time.Clock = pygame.time.Clock()

    login_font: FontManager = FontManager("jeu/assets/fonts/Truculenta.ttf")

    # Initializing on-screen elements #
    login_popup: Popup = Popup(screen, "Account", (500, 580), "#0575BB")

    username_textbox = Textbox(
        screen=screen,
        position=(screen.get_size()[0]//2, 300),
        placeholder_text="Username",
        font=login_font.get_font(75),
        size=(370, 100)
    )
    password_textbox = Textbox(
        screen=screen,
        position=(screen.get_size()[0]//2, 425),
        placeholder_text="Password",
        font=login_font.get_font(75),
        size=(370, 100)
    )

    login_button = Button(
        screen=screen,
        image=pygame.image.load("jeu/assets/images/Login Rect.png"),
        position=(520, 550),
        text="Login",
        font=login_font.get_font(50),
        color="#000000",
        hover_color="#555555",
        action=login_handler
    )
    register_button = Button(
        screen=screen,
        image=pygame.image.load("jeu/assets/images/Login Rect.png"),
        position=(770, 550),
        text="Register",
        font=login_font.get_font(50),
        color="#000000",
        hover_color="#555555",
        action=register_handler
    )

    ui_elements: list[UI] = [login_popup, username_textbox, password_textbox,
                             register_button, login_button]

    while active:
        print(int(clock.get_fps()), end=" FPS    \r")

        for event in pygame.event.get():
            match (event.type):
                case pygame.QUIT:
                    quit()
                case pygame.MOUSEBUTTONDOWN:
                    # Clear FPS counter from console
                    print("            ", end="\r")
            for ui_element in ui_elements:
                ui_element.update(event)
        for ui_element in ui_elements:
            ui_element.update_render()

        pygame.display.update()
        clock.tick()
