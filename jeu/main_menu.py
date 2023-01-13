import sys

import pygame
from jeu.login_screen import login_screen
from jeu.options_screen import options_screen
from jeu.game import game
from jeu.ui.button import Button
from jeu.ui.popup import Popup
from jeu.ui.textbox import Textbox
from jeu.ui.ui import UI
from jeu.utils.font_manager import FontManager
from jeu.utils.assets_import import resource_path


def main_menu(screen: pygame.surface.Surface):
    """Main menu of the game.

    Args:
        screen (pygame.surface.Surface): Screen to display the menu on
    """
    clock: pygame.time.Clock = pygame.time.Clock()

    pygame.display.set_caption("Menu")

    menu_font: FontManager = FontManager(resource_path("jeu/assets/fonts/Truculenta.ttf"))

    def quit():
        pygame.quit()
        sys.exit()

    def play_button_handler(screen): 

        """
        Popup:
        +-------------------------+
        |          Size           |
        |   (   Custom Size   )   |
        | [ 3x3 ] [ 5x5 ] [ 7x7 ] |
        +-------------------------+
        """
        # 3x3, 5x5, 7x7
        size_popup = Popup(
            screen=screen,
            title="Size",
            size=(1280//2, 720//2.5),
            color="#0575BB"
        )

        size_popup_3x3_button = Button(
            screen=size_popup.surface,
            image=None,
            position=(size_popup.surface.get_size()[0]//2*0.5, size_popup.surface.get_size()[1]//1.25),
            text="3x3",
            font=menu_font.get_font(56),
            color="white",
            hover_color="black",
            action = lambda: game(screen, size=(3, 3))
        )

        size_popup_5x5_button = Button(
            screen=size_popup.surface,
            image=None,
            position=(size_popup.surface.get_size()[0]//2, size_popup.surface.get_size()[1]//1.25),
            text="5x5",
            font=menu_font.get_font(56),
            color="white",
            hover_color="black",
            action = lambda: game(screen, size=(5, 5))
        )

        size_popup_7x7_button = Button(
            screen=size_popup.surface,
            image=None,
            position=(size_popup.surface.get_size()[0]//2*1.5, size_popup.surface.get_size()[1]//1.25),
            text="7x7",
            font=menu_font.get_font(56),
            color="white",
            hover_color="black",
            action = lambda: game(screen, size=(7, 7))
        )


        size_popup_custom_size_x_textbox = Textbox(
            screen=size_popup.surface,
            position=(size_popup.surface.get_size()[0]//2, size_popup.surface.get_size()[1]//2),
            placeholder_text="a",
            placeholder_color="#424242",
            size=(75,75),
            font=menu_font.get_font(56),
            text_color="black",
            background_color="white",
            max_char = 2,
            accepted_chars = ["0","1","2","3","4","5","6","7","8","9"]
        )

        size_popup.add_ui_element(size_popup_3x3_button)
        size_popup.add_ui_element(size_popup_5x5_button)
        size_popup.add_ui_element(size_popup_7x7_button)
        size_popup.add_ui_element(size_popup_custom_size_x_textbox)

        size_popup.run()

    # Initializing on-screen elements #
    background: pygame.surface.Surface = pygame.image.load(resource_path("jeu/assets/images/menu_background.png"))

    menu_text: pygame.surface.Surface = menu_font.get_font(
        100).render("MAIN MENU", True, "#EEEEEE")
    menu_rect: pygame.rect.Rect = menu_text.get_rect(center=(640, 75))

    play_button = Button(
        screen=screen,
        image=pygame.image.load(resource_path("jeu/assets/images/Play Rect.png")),
        position=(640, 250),
        text="PLAY",
        font=menu_font.get_font(75),
        color="#FFFFFF",
        hover_color="#d7fcd4",
        action=lambda: play_button_handler(screen)
    )
    options_button = Button(
        screen=screen,
        image=pygame.image.load(resource_path("jeu/assets/images/Options Rect.png")),
        position=(640, 400),
        text="OPTIONS",
        font=menu_font.get_font(75),
        color="#FFFFFF",
        hover_color="#d7fcd4",
        action=lambda: options_screen(screen)
    )
    quit_button = Button(
        screen=screen,
        image=pygame.image.load(resource_path("jeu/assets/images/Quit Rect.png")),
        position=(640, 550),
        text="QUIT",
        font=menu_font.get_font(75),
        color="#FFFFFF",
        hover_color="#d7fcd4",
        action=quit
    )

    account_button = Button(screen=screen, image=pygame.image.load(resource_path("jeu/assets/images/User.png")),
                            position=(1280-75, 75),
                            text=" ",
                            font=menu_font.get_font(75),
                            color="#FFFFFF",
                            hover_color="#FFFFFF",
                            action=lambda: login_screen(screen)
                            )

    menu_buttons: tuple[UI, ...] = (account_button, play_button, options_button, quit_button)

    while True:
        print(int(clock.get_fps()), end=" FPS    \r")
        screen.blit(background, (0, 0))
        screen.blit(menu_text, menu_rect)

        for event in pygame.event.get():
            match (event.type):
                case pygame.QUIT:
                    quit()
                case pygame.MOUSEBUTTONDOWN:
                    # Clear FPS counter from console
                    print("            ", end="\r")
            for button in menu_buttons:
                button.update(event)
        for button in menu_buttons:
            button.update_render()
        pygame.display.update()
        clock.tick()
