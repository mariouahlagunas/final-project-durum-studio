import arcade
import math


class Bullet(arcade.Sprite):

    def __init__(self, start_x, start_y, end_x, end_y, scale, damage, speed):

        super().__init__(scale=scale)

        self.center_x = start_x
        self.center_y = start_y

        x_diff = end_x - start_x
        y_diff = end_y - start_y
        angle = math.atan2(y_diff, x_diff)
        self.angle = math.degrees(angle)

        self.change_x = math.cos(angle) * speed
        self.change_y = math.sin(angle) * speed

        self.damage = damage


    def get_damage(self):
        return self.damage