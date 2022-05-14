from src.Bullet import *

class Bullet_Electricity(Bullet):

    def __init__(self, start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed):
        scale = SCALE_BULLET_ELECTRICITY * multiplier_scale
        damage = DAMAGE_BULLET_ELECTRICITY * multiplier_damage
        speed = SPEED_BULLET_ELECTRICITY * multiplier_speed

        super().__init__(start_x, start_y, scale, damage, speed)

        super().liner_move_with_rotation(start_x, start_y, end_x, end_y)

        self.moved_textures = super().load_textures(TEXTURES_PATH_BULLET_ELECTRICITY, "move", NUM_MOVE_TEXTURES_BULLET_ELECTRICITY)

        self.hit_textures = super().load_textures(TEXTURES_PATH_BULLET_ELECTRICITY, "hit", NUM_HIT_TEXTURES_BULLET_ELECTRICITY)

        super().set_textures(self.moved_textures)


    def draw(self):
        super().draw()


    def update(self):
        super().update()
        super().update_animation()

        if super().is_hit():
            if not super().is_animated():
                super().dead_bullet()


    def collision(self):
        super().set_textures(self.hit_textures, loop_textures = False)
        super().stop_move()
        super().hit_bullet()