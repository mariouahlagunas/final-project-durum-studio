from src.Bullet import *

class Bullet_Fire(Bullet):

    def __init__(self, start_x, start_y, end_x, end_y, multiplier_timer, multiplier_scale, multiplier_damage, multiplier_speed):
        multiplier_timer /= 60
        if multiplier_timer < 1:
            multiplier_timer = 1
        elif multiplier_timer > MAX_MULTIPLIER_TIMER_BULLET_FIRE:
            multiplier_timer = MAX_MULTIPLIER_TIMER_BULLET_FIRE

        scale = SCALE_BULLET_FIRE * multiplier_scale * multiplier_timer
        damage = DAMAGE_BULLET_FIRE * multiplier_damage * multiplier_timer
        speed = SPEED_BULLET_FIRE * multiplier_speed

        super().__init__(start_x, start_y, scale, damage, speed)

        super().liner_move_with_rotation(start_x, start_y, end_x, end_y)

        self.moved_textures = super().load_textures(TEXTURES_PATH_BULLET_FIRE, "move", NUM_MOVE_TEXTURES_BULLET_FIRE)

        self.hit_textures = super().load_textures(TEXTURES_PATH_BULLET_FIRE, "hit", NUM_HIT_TEXTURES_BULLET_FIRE)

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