import arcade
import math

from src.Globals import *


class Bullet(arcade.Sprite):

    def __init__(self, center_x, center_y, scale, damage, speed):
        super().__init__(scale=scale)

        self.center_x = center_x
        self.center_y = center_y
        self.change_x = 0
        self.change_y = 0

        self.damage = damage
        self.speed = speed

        self.texture = None
        self.textures = None
        self.cur_texture = 0
        self.loop_textures = True
        self.animated = True

        self.moved = True
        self.stopped = False
        self.hit = False

        self.alive = True
        self.dead = False


    def liner_move_without_rotation(self, start_x, start_y, end_x, end_y):
        x_diff = end_x - start_x
        y_diff = end_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed


    def liner_move_with_rotation(self, start_x, start_y, end_x, end_y):
        x_diff = end_x - start_x
        y_diff = end_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.angle = math.degrees(angle)

        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed


    def stop_move(self):
        self.change_x = 0
        self.change_y = 0


    def load_textures(self, path_textures, type_textures, num_textures):
        textures = []
        for i in range(num_textures):
            texture = arcade.load_texture(f"{path_textures}_{type_textures}{i}.png")
            textures.append(texture)

        return textures


    def set_textures(self, textures, cur_texture = 0, loop_textures = True):
        self.textures = textures
        self.cur_texture = cur_texture
        self.loop_textures = loop_textures
        self.animated = True


    def update_animation(self):
        # Animación del movimiento de la bala
        frame = self.cur_texture // UPDATES_PER_FRAME_SHOOT
        self.texture = self.textures[frame]

        self.cur_texture += 1
        if self.cur_texture > (len(self.textures) - 1) * UPDATES_PER_FRAME_SHOOT:
            if self.loop_textures:
                self.cur_texture = 0
            else:
                self.animated = False


    def is_animated(self):
        return self.animated


    def get_damage(self):
        return self.damage


    def get_speed(self):
        return self.speed


    def stopped_bullet(self):
        self.moved = False
        self.stopped = True


    def hit_bullet(self):
        self.moved = False
        self.stopped = False
        self.hit = True


    def is_moved(self):
        return self.moved


    def is_stopped(self):
        return self.stopped


    def is_hit(self):
        return self.hit


    def dead_bullet(self):
        self.alive = False
        self.dead = True


    def is_alive(self):
        return self.alive


    def is_dead(self):
        return self.dead