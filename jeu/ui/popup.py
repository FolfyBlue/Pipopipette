from __future__ import annotations
from re import S

import pygame
from jeu.utils.font_manager import FontManager
from jeu.ui.button import Button


class Popup():
    def __init__(self: Popup, screen: pygame.surface.Surface, title: str, size: tuple[float, float], color: str = "white") -> None:
        self.active = True  
        self.screen = screen
        self.color = color
        self.font: FontManager = FontManager("jeu/assets/fonts/Truculenta.ttf")
        self.background = pygame.Surface(size)
        self.title: pygame.surface.Surface = self.font.get_font(100).render(title, True, "#EEEEEE")
        self.title_rect: pygame.rect.Rect = self.title.get_rect(center=(self.background.get_rect().center[0], 50))

        close_button_img = pygame.image.load("jeu/assets/images/close.png")
        offset = (
            (screen.get_width()-size[0])/2,
            (screen.get_height()-size[1])/2,
        )
        self.close_button = Button(
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
        self.active = False

    def update_render(self):
            if not self.active: return
            self.background.fill(self.color)
            
            self.close_button.update_render(self.background)
            self.background.blit(self.title, self.title_rect)

            rect = self.background.get_rect(center=self.screen.get_rect().center)
            self.screen.blit(self.background, rect)

    def update(self, event):
            if not self.active: return
            self.close_button.update(event)

