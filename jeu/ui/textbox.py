from __future__ import annotations

import pygame


class Textbox():
    def __init__(self: Textbox, position: tuple[int, int], placeholder_text: str, font: pygame.font.Font, size: tuple[int, int], text_color: str = "Black", background_color: str = "White", placeholder_color: str = "#E4E4E4") -> None:
        """Textbox UI element

        Args:
            position (tuple[int, int]): X and Y position of the textbox
            placeholder_text (str): Text to display when the textbox is empty
            font (pygame.font.Font): Font to use for the text
            color (str): Color of the text
        """
        self.focused: bool = False
        self.text: str = ""
        self.size: tuple[int, int] = size
        self.center: tuple[float, float] = tuple(coord/2 for coord in self.size)
        self.surface = pygame.Surface(self.size)

        self.position = position
        self.font = font
        self.text_color = text_color
        self.placeholder_color = placeholder_color
        self.background_color = background_color
        self.placeholder_text = placeholder_text
        self.placeholder_text_render = self.font.render(
            self.placeholder_text, True, self.placeholder_color)
        self.rect = self.surface.get_rect(center=self.position)
        self.placeholder_text_rect = self.placeholder_text_render.get_rect(
            center=self.center)

    def update_render(self: Textbox, screen: pygame.surface.Surface) -> None:
        """Updates the button

        Args:
            screen (pygame.surface.Surface): Screen to update the button on
        """
        self.surface.fill(self.background_color)
        if self.text == "":
            self.surface.blit(self.placeholder_text_render,
                              self.placeholder_text_rect)
        else:
            text_render = self.font.render(self.text, True, self.text_color)
            self.surface.blit(
                text_render, text_render.get_rect(center=self.center))
        screen.blit(self.surface, self.rect)
    
    def _process_input(self, event: pygame.event.Event):
        match (event.key):
            case pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            case pygame.K_ESCAPE:
                self.focused = False
            case _:
                self.text += event.unicode

    def update(self: Textbox, event: pygame.event.Event):
        match (event.type):
            case pygame.MOUSEBUTTONUP:
                mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    self.repeat_settings = pygame.key.get_repeat()
                    pygame.key.set_repeat(500, 50)
                    self.focused = True
                else:
                    try:
                        pygame.key.set_repeat(*self.repeat_settings)
                    except:
                        pass
                    self.focused = False
            case pygame.KEYDOWN:
                if self.focused:
                    self._process_input(event)