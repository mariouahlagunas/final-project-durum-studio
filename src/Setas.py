import arcade

from src.Globals import *


class setas(arcade.Sprite):
    def __init__(self,x_SETAS, y_SETAS):

        super().__init__(IMG_SETAS, SCALE_SETAS)

        self.center_x = x_SETAS
        self.center_y = y_SETAS