from src.Bullet import *

class Bullet_Water(Bullet):

    def __init__(self, start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed):
        scale = SCALE_BULLET_WATER * multiplier_scale
        damage = DAMAGE_BULLET_WATER * multiplier_damage
        speed = SPEED_BULLET_WATER * multiplier_speed

        super().__init__(start_x, start_y, scale, damage, speed)

        super().liner_move_with_rotation(start_x, start_y, end_x, end_y)

        self.moved_textures = super().load_textures(TEXTURES_PATH_BULLET_WATER, "move", NUM_MOVE_TEXTURES_BULLET_WATER)
        self.moved_time = TIME_MOVE_BULLET_WATER

        self.moved_stopped_transaction_textures = super().load_textures(TEXTURES_PATH_BULLET_WATER, "transaction", NUM_TRANSACTION_TEXTURES_BULLET_WATER)

        self.stopped_textures = super().load_textures(TEXTURES_PATH_BULLET_WATER, "not_move", NUM_STOP_TEXTURES_BULLET_WATER)
        self.stopped_time = TIME_STOP_BULLET_WATER

        self.hit_textures = self.moved_stopped_transaction_textures

        super().set_textures(self.moved_textures)


    def draw(self):
        super().draw()


    def update(self):
        super().update()
        super().update_animation()

        if super().is_moved():
            if self.moved_time > 0:
                self.moved_time -= 1
            elif self.moved_time == 0:
                self.moved_time -= 1
                super().set_textures(self.moved_stopped_transaction_textures, loop_textures = False)
            else:
                if not super().is_animated():
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
                super().set_textures(self.stopped_textures)
                super().stopped_bullet()


    def collision(self):
        super().set_textures(self.hit_textures, loop_textures = False)
        super().stop_move()
        super().hit_bullet()