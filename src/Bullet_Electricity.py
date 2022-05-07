import arcade

from src.Globals import *
from src.Bullet import *

class Bullet_Electricity(Bullet):

    def __init__(self, start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed):
        scale = SCALE_BULLET_ELECTRICITY * multiplier_scale
        damage = DAMAGE_BULLET_ELECTRICITY * multiplier_damage
        speed = SPEED_BULLET_ELECTRICITY * multiplier_speed

        super().__init__(start_x, start_y, end_x, end_y, scale, damage, speed)

        self.texture = None
        self.cur_texture = 0

        self.move_textures = []
        for i in range(NUM_MOVE_TEXTURES_BULLET_ELECTRICITY):
            texture = arcade.load_texture(f"{TEXTURES_PATH_ELECTRICITY}_move{i}.png")
            self.move_textures.append(texture)


    def draw(self):
        super().draw()


    def update(self):
        super().update()

        self.cur_texture += 1
        if self.cur_texture > (len(self.move_textures) - 1) * UPDATES_PER_FRAME_SHOOT:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME_SHOOT
        self.texture = self.move_textures[frame]