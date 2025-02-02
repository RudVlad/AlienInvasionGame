import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msq(msg)

    def _prep_msq(self, msg):
        self.msq_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msq_image_rect = self.msq_image.get_rect()
        self.msq_image_rect.center = self.rect.center

    def draw_button(self):
        """
        border_rect = self.rect
        border_rect.height = self.rect.height + 2
        self.screen.fill((0, 0, 0), border_rect)
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msq_image, self.msq_image_rect)
