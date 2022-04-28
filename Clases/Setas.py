import arcade
import Clases.Globals
class setas(arcade.Sprite):
    def __init__(self,x_SETAS, y_SETAS):
        IMG_SETAS= ":resources:images/topdown_tanks/tank_green.png"
        SCALE_SETAS=.8
        super().__init__(IMG_SETAS, SCALE_SETAS)

        self.center_x = x_SETAS
        self.center_y = y_SETAS
