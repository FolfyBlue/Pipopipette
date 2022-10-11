from __future__ import annotations

from typing import Callable

import pygame


class Button():
    def __init__(self: Button, image: pygame.surface.Surface | None, position: tuple[float, float], text: str, font: pygame.font.Font, color: str, hover_color: str, action: Callable = lambda: None) -> None:
        """Button UI elements

        Args:
            image (pygame.surface.Surface | None): Image to use as background
            position (tuple[int, int]): X and Y position of the button
            text (str): Text to display on the button
            font (pygame.font.Font): Font to use for the text
            color (str): Color of the text
            hover_color (str): Color of the text when hovering
            action (Callable): Function to call upon button click
        """
        self.image = image
        self.position = position
        self.font = font
        self.color, self.hover_color = color, hover_color
        self.text = text
        self.text_render = self.font.render(self.text, True, self.color)
        self.action = action
        if not self.image:
            self.image = self.text_render
        self.rect = self.image.get_rect(center=self.position)
        self.text_rect = self.text_render.get_rect(center=self.position)

    def update_render(self: Button, screen: pygame.surface.Surface) -> None:
        """Updates the button

        Args:
            screen (pygame.surface.Surface): Screen to update the button on
        """
        if self.image:
            screen.blit(self.image, self.rect)
        screen.blit(self.text_render, self.text_rect)

    def update(self: Button, event: pygame.event.Event) -> bool:
        """Updates the button according to the given event.

        Args:
            event (pygame.event.Event): Event to check for

        Returns:
            bool: Weither the button was clicked or not 
        """
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        match (event.type):
            case pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(mouse_pos):
                    self.action()
                    return True
            case pygame.MOUSEMOTION:
                if self.rect.collidepoint(mouse_pos):
                    self.text_render = self.font.render(
                        self.text, True, self.hover_color)
                else:
                    self.text_render = self.font.render(
                        self.text, True, self.color)

        return False
