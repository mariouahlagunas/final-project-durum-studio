import arcade

from src.Globals import *


class Escudo(arcade.Sprite):

    def __init__(self, x_SETA, y_SETA):

        super().__init__(IMG_ESCUDO, SCALE_ESCUDO)

        self.center_x = x_SETA
        self.center_y = y_SETA