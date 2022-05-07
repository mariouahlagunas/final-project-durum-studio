import arcade
import math

from src.Globals import *


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

        self.texture = None
        self.cur_texture = 0

        self.death = False
        self.death_of_death = False



    def load_textures(self, path_textures, type_textures, num_textures):
        textures = []
        for i in range(num_textures):
            texture = arcade.load_texture(f"{path_textures}_{type_textures}{i}.png")
            textures.append(texture)

        return textures


    def update_animation_move(self, textures, delta_time: float = 1 / 60):
        # Animación del movimiento de la bala
        self.cur_texture += 1
        if self.cur_texture > (len(textures) - 1) * UPDATES_PER_FRAME_SHOOT:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME_SHOOT
        self.texture = textures[frame]


    def get_damage(self):
        return self.damage


    def not_move(self):
        self.change_x = 0
        self.change_y = 0


    def alive(self):
        if self.death:
            return False
        else:
            return True


    def dead(self):
        if self.death_of_death:
            return True
        else:
            return False


    def sprite_death(self):
        self.death = True


    def spite_death_of_death(self):
        self.death_of_death = True