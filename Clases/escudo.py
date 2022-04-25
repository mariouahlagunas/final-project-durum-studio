import arcade
import Globals
class Escudo(arcade.Sprite):
    def __init__(self, x_SETA, y_SETA):
        IMG_ESCUDO = ":resources:images/items/coinGold.png"
        SCALE_ESCUDO = .6
        super().__init__(IMG_ESCUDO, SCALE_ESCUDO)

        self.center_x = x_SETA
        self.center_y = y_SETA

