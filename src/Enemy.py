import random
import math

from src.Character import *

class Enemy(Character):

    def __init__(self, center_x, center_y, change_x, change_y, objetive):
        super().__init__(SCALE_ENEMY, SPEED_ENEMY, HP_ENEMY, center_x, center_y, change_x, change_y)

        self.idle_textures = [arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_idle.png"),
                              arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_idle.png", flipped_horizontally=True)]

        self.walk_textures = []
        for i in range(NUM_WALK_TEXTURES_ENEMY):
            texture = [arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_walk{i}.png"),
                       arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_walk{i}.png", flipped_horizontally=True)]
            self.walk_textures.append(texture)

        self.attack_textures = []
        for i in range(NUM_ATTACK_TEXTURES_ENEMY):
            texture = [arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_climb{i}.png"),
                       arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_climb{i}.png", flipped_horizontally=True)]
            self.attack_textures.append(texture)

        self.objetive = objetive
        self.time_for_shoot = random.randint(100, 500)


    def draw(self):
        super().draw()
        super().print_life()


    def update(self):
        super().update()
        super().update_animation_walk(self.idle_textures, self.walk_textures)


    def updateIA(self, end_x, end_y):
        distancia = self.distance()

        if distancia < 600:
            if self.time_for_shoot == 0:
                self.time_for_shoot = random.randint(100, 500)
                return self.attack_shoot(end_x, end_y)
            else:
                self.time_for_shoot -= 1


    def distance(self):
        return math.sqrt((self.center_x - self.objetive.center_x) ** 2 + (self.center_y - self.objetive.center_y) ** 2)



    def attack_shoot(self, end_x, end_y, timer_mouse=0):
        type = "electricity"
        multiplier_scale = 1
        multiplier_damage = 1
        multiplier_speed = 1

        bullet = super().shoot(end_x, end_y, type, timer_mouse, multiplier_scale, multiplier_damage, multiplier_speed)

        return bullet