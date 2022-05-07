from src.Bullet import *

class Bullet_Air(Bullet):

    def __init__(self, start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed):
        scale = SCALE_BULLET_AIR * multiplier_scale
        damage = DAMAGE_BULLET_AIR * multiplier_damage
        speed = SPEED_BULLET_AIR * multiplier_speed

        super().__init__(start_x, start_y, end_x, end_y, scale, damage, speed)

        self.life_move_textures = super().load_textures(TEXTURES_PATH_BULLET_AIR,"move", NUM_MOVE_TEXTURES_BULLET_AIR)
        self.death_move_textures = super().load_textures(TEXTURES_PATH_BULLET_ELECTRICITY, "move", NUM_MOVE_TEXTURES_BULLET_ELECTRICITY)

        self.time_life_move = TIME_LIFE_MOVE_BULLET_AIR
        self.time_death_move = TIME_DEATH_MOVE_BULLET_AIR


    def draw(self):
        super().draw()


    def update(self):
        super().update()

        if self.time_life_move >= 0:
            if self.time_life_move == 0:
                super().not_move()
                super().sprite_death()
            self.time_life_move -= 1
            super().update_animation_move(self.life_move_textures)
        else:
            if self.time_death_move >= 0:
                self.time_death_move -= 1
                super().update_animation_move(self.death_move_textures)
            else:
                super().spite_death_of_death()