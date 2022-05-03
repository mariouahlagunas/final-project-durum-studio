import arcade
import Clases.Globals
class Bullet_num(arcade.Sprite):
    def __init__(self, tipo, x_BULLET, y_BULLET):
        imagen_b=""
        scala_b=""
        if tipo=="azul":
            imagen_b = ":resources:images/space_shooter/laserBlue01.png"
            scala_b = .6
        if tipo=="rojo":
            imagen_b = ":resources:images/space_shooter/laserRed01.png"
            scala_b = .6
        super().__init__(imagen_b, scala_b)

        self.center_x = x_BULLET
        self.center_y = y_BULLET