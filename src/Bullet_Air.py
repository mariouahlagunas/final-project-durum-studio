from src.Bullet import *

class Bullet_Air(Bullet):

    def __init__(self, start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed):
        scale = SCALE_BULLET_AIR * multiplier_scale
        damage = DAMAGE_BULLET_AIR * multiplier_damage
        speed = SPEED_BULLET_AIR * multiplier_speed

        super().__init__(start_x, start_y, scale, damage, speed)

        super().liner_move_without_rotation(start_x, start_y, end_x, end_y)

        self.moved_textures = super().load_textures(TEXTURES_PATH_BULLET_AIR, "move", NUM_MOVE_TEXTURES_BULLET_AIR)
        self.moved_time = TIME_MOVE_BULLET_AIR

        self.stopped_textures = self.moved_textures
        self.stopped_time = TIME_STOP_BULLET_AIR

        self.hit_textures = super().load_textures(TEXTURES_PATH_BULLET_AIR, "hit", NUM_HIT_TEXTURES_BULLET_AIR)

        super().set_textures(self.moved_textures)


    def draw(self):
        super().draw()


    def update(self):
        super().update()
        super().update_animation()

        if super().is_moved():
            if self.moved_time > 0:
                self.moved_time -= 1
            else:
                super().set_textures(self.stopped_textures)
                super().stop_move()
                super().stopped_bullet()

        if super().is_stopped():
            if self.stopped_time > 0:
                self.stopped_time -= 1
            else:
                super().dead_bullet()

        if super().is_hit():
            if not super().is_animated():
                super().dead_bullet()


    def collision(self):
        super().set_textures(self.hit_textures, loop_textures = False)
        super().stop_move()
        super().hit_bullet()