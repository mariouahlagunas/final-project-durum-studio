import arcade

from src.Globals import *


class Bullet_Fire(Bullet):

    def __init__(self, start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed):
        scale = SCALE_BULLET_FIRE * multiplier_scale
        damage = DAMAGE_BULLET_FIRE * multiplier_damage
        speed = SPEED_BULLET_FIRE * multiplier_speed

        super().__init__(start_x, start_y, end_x, end_y, scale, damage, speed)