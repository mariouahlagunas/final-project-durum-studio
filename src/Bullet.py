import arcade
import math

from src.Globals import *


class Bullet(arcade.Sprite):

    def __init__(self, start_x, start_y, end_x, end_y, type, multiplier_scale, multiplier_damage, multiplier_speed):

        if type == "fire":
            img = IMG_BULLET_FIRE
            scale = SCALE_BULLET_FIRE * multiplier_scale
            damage = DAMAGE_BULLET_FIRE * multiplier_damage
            speed =  SPEED_BULLET_FIRE * multiplier_speed
        elif type == "water":
            img = IMG_BULLET_WATER
            scale = SCALE_BULLET_WATER * multiplier_scale
            damage = DAMAGE_BULLET_WATER * multiplier_damage
            speed = SPEED_BULLET_WATER * multiplier_speed
        elif type == "electricity":
            printf("electricidad")
            #completar
        elif type == "air":
            printf("aire")
            #completar
        else:
            printf("Error")
            #completar

        super().__init__(img, scale)

        self.center_x = start_x
        self.center_y = start_y

        x_diff = end_x - start_x
        y_diff = end_y - start_y
        angle = math.atan2(y_diff, x_diff)
        self.angle = math.degrees(angle)

        self.change_x = math.cos(angle) * speed
        self.change_y = math.sin(angle) * speed

        self.damage = damage


    def damage(self):
        return self.damage