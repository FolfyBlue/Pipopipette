import sys

import pygame
from jeu.ui.button import Button
from jeu.ui.textbox import Textbox
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
    background: pygame.surface.Surface = pygame.image.load(
        "jeu/assets/images/login_background.png")

    login_text: pygame.surface.Surface = login_font.get_font(
        100).render("Account", True, "#EEEEEE")
    login_text_rect: pygame.rect.Rect = login_text.get_rect(
        center=(screen.get_size()[0]//2, 150))

    username_textbox = Textbox(
        position=(screen.get_size()[0]//2, 300),
        placeholder_text="Username",
        font=login_font.get_font(75),
        size=(370, 100)
    )
    password_textbox = Textbox(
        position=(screen.get_size()[0]//2, 425),
        placeholder_text="Password",
        font=login_font.get_font(75),
        size=(370, 100)
    )

    close_button = Button(
        image=pygame.image.load("jeu/assets/images/close.png"),
        position=(screen.get_size()[0]/1.5, 100),
        text=" ",
        font=login_font.get_font(50),
        color="#000000",
        hover_color="#555555",
        action=close_login_screen
    )

    login_button = Button(image=pygame.image.load("jeu/assets/images/Login Rect.png"),
                          position=(520, 550),
                          text="Login",
                          font=login_font.get_font(50),
                          color="#000000",
                          hover_color="#555555",
                          action=login_handler
                          )
    register_button = Button(image=pygame.image.load("jeu/assets/images/Login Rect.png"),
                             position=(770, 550),
                             text="Register",
                             font=login_font.get_font(50),
                             color="#000000",
                             hover_color="#555555",
                             action=register_handler
                             )

    ui_elements = [username_textbox, password_textbox,
                   register_button, login_button, close_button]

    while active:
        print(int(clock.get_fps()), end=" FPS    \r")
        screen.blit(background, (0, 0))

        screen.blit(login_text, login_text_rect)

        for event in pygame.event.get():
            match (event.type):
                case pygame.QUIT:
                    quit()
                case pygame.MOUSEBUTTONDOWN:
                    # Clear FPS counter from console
                    print("            ", end="\r")
            for textbox in ui_elements:
                textbox.update(event)
        for textbox in ui_elements:
            textbox.update_render(screen)

        pygame.display.update()
        clock.tick()
