from __future__ import annotations

import pygame
from jeu.ui.ui import UI
from jeu.utils.font_manager import FontManager
from jeu.ui.button import Button


class Popup(UI):
    def __init__(self: Popup, screen: pygame.surface.Surface, title: str, size: tuple[float, float], color: str = "white") -> None:
        """Centered popup that appears over the game screen

        Args:
            screen (pygame.surface.Surface): Screen to update the popup onto
            title (str): Title of the popup
            size (tuple[float, float]): Size of the popup
            color (str, optional): Background color of the popup. Defaults to "white".
        """
        super().__init__(screen)
        self.active = True  
        self.color = color
        self.font: FontManager = FontManager("jeu/assets/fonts/Truculenta.ttf")
        self.background = pygame.Surface(size)
        self.title: pygame.surface.Surface = self.font.get_font(100).render(title, True, "#EEEEEE")
        self.title_rect: pygame.rect.Rect = self.title.get_rect(center=(self.background.get_rect().center[0], 50))
        self.elements: list = []

        close_button_img = pygame.image.load("jeu/assets/images/close.png")
        offset = (
            (screen.get_width()-size[0])/2,
            (screen.get_height()-size[1])/2,
        )
        self.close_button = Button(
            screen=self.background,
            image=close_button_img,
            position=(self.background.get_width()-25, 25),
            text=" ",
            font=self.font.get_font(50),
            color="#000000",
            hover_color="#555555",
            action=self.close,
            detection_offset=offset
        )

    def close(self: Popup):
        """Marks the popup as inactive
        """
        self.active = False

    def update_render(self):
        """Updates the popup's render
        """
        if not self.active: return
        self.background.fill(self.color)
        
        self.close_button.update_render()
        self.background.blit(self.title, self.title_rect)

        rect = self.background.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(self.background, rect)

    def update(self, event):
        """Updates the popup according to the given event.

        Args:
            event (pygame.event.Event): Event to check for
        """
        if not self.active: return
        self.close_button.update(event)
