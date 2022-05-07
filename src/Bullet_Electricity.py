from src.Bullet import *

class Bullet_Electricity(Bullet):

    def __init__(self, start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed):
        scale = SCALE_BULLET_ELECTRICITY * multiplier_scale
        damage = DAMAGE_BULLET_ELECTRICITY * multiplier_damage
        speed = SPEED_BULLET_ELECTRICITY * multiplier_speed

        super().__init__(start_x, start_y, end_x, end_y, scale, damage, speed)

        self.move_textures = super().load_textures(TEXTURES_PATH_BULLET_ELECTRICITY,"move", NUM_MOVE_TEXTURES_BULLET_ELECTRICITY)


    def draw(self):
        super().draw()


    def update(self):
        super().update()

        super().update_animation_move(self.move_textures)