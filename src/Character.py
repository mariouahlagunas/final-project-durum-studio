import arcade

from src.Globals import *
from src.Bullet_Electricity import *


class Character(arcade.Sprite):

    def __init__(self, scale, speed, hp, center_x, center_y, change_x, change_y):
        super().__init__(scale=scale)

        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y

        self.movement_speed_normal = speed
        self.movement_speed_now = speed

        self.hp_max = hp
        self.hp_now = hp

        self.texture = None
        self.face_direction = RIGHT_FACING
        self.walk = True
        self.cur_texture_walk = 0
        self.attack = False
        self.cur_texture_attack = 0


    def sprite_walk(self):
        self.walk = True
        self.attack = False


    def sprite_attack(self):
        self.walk = False
        self.attack = True


    def update_animation_walk(self, idle_textures, walk_textures, delta_time: float = 1 / 60):
        if self.walk:
            # Comprobamos la dirección de movimiento
            if self.change_x < 0 and self.face_direction == RIGHT_FACING:
                self.face_direction = LEFT_FACING
            elif self.change_x > 0 and self.face_direction == LEFT_FACING:
                self.face_direction = RIGHT_FACING

            # Animación de parado
            if self.change_x == 0 and self.change_y == 0:
                self.texture = idle_textures[self.face_direction]
                return

            # Animación de andar
            self.cur_texture_walk += 1
            if self.cur_texture_walk > (len(walk_textures) - 1) * UPDATES_PER_FRAME_WALK:
                self.cur_texture_walk = 0
            frame = self.cur_texture_walk // UPDATES_PER_FRAME_WALK
            direction = self.face_direction
            self.texture = self.walk_textures[frame][direction]


    def update_animation_attack(self, attack_textures, delta_time: float = 1 / 60):
        if self.attack:
            # Comprobamos la dirección del ataque
            if self.change_x < 0 and self.face_direction == RIGHT_FACING:
                self.face_direction = LEFT_FACING
            elif self.change_x > 0 and self.face_direction == LEFT_FACING:
                self.face_direction = RIGHT_FACING

            # Animación de atacar
            self.cur_texture_attack += 1
            if self.cur_texture_attack > (len(attack_textures) - 1) * UPDATES_PER_FRAME_ATTACK:
                self.cur_texture_attack = 0
            frame = self.cur_texture_attack // UPDATES_PER_FRAME_ATTACK
            direction = self.face_direction
            self.texture = self.attack_textures[frame][direction]
            if self.cur_texture_attack == 0:
                self.sprite_walk()


    def change_movement_speed(self, multiplier):
        self.movement_speed_now = self.movement_speed_normal * multiplier


    def not_move(self):
        self.change_x = 0
        self.change_y = 0


    def move_up(self):
        self.change_y = self.movement_speed_now


    def move_down(self):
        self.change_y = -self.movement_speed_now


    def move_left(self):
        self.change_x = -self.movement_speed_now


    def move_right(self):
        self.change_x = self.movement_speed_now


    def max_hp(self):
        return self.hp_max


    def now_hp(self):
        return self.hp_now


    def alive(self):
        if self.hp_now > 0:
            return True
        else:
            return False


    def lose_life(self, amount):
        self.hp_now -= amount
        if self.hp_now < 0:
            self.hp_now = 0


    def gain_life(self, amount):
        self.hp_now += amount
        if self.hp_now > self.hp_max:
            self.hp_max


    def print_life(self):
        healthbar_height = HEALTHBAR_HEIGHT
        healthbar_height_framework = HEALTHBAR_HEIGHT + 4
        healthbar_width = HEALTHBAR_WIDTH * self.hp_now
        healthbar_width_framework = HEALTHBAR_WIDTH * self.hp_max + 4

        if self.hp_now > self.hp_max * 0.5:
            healthbar_color = arcade.color.GREEN
        elif self.hp_now > self.hp_max * 0.25:
            healthbar_color = arcade.color.YELLOW
        else:
            healthbar_color = arcade.color.RED
        healthbar_color_framework = arcade.color.BLACK

        arcade.draw_rectangle_filled(center_x=self.center_x,
                                     center_y=self.top + 5,
                                     width=healthbar_width_framework,
                                     height=healthbar_height_framework,
                                     color=healthbar_color_framework)

        arcade.draw_rectangle_filled(center_x=self.center_x - HEALTHBAR_WIDTH * 0.5 * (self.hp_max - self.hp_now),
                                     center_y=self.top + 5,
                                     width=healthbar_width,
                                     height=healthbar_height,
                                     color=healthbar_color)


    def shoot(self, end_x, end_y, type, multiplier_scale, multiplier_damage, multiplier_speed):
        self.sprite_attack()

        start_x = self.center_x
        start_y = self.center_y

        bullet = None
        if type == "fire":
            bullet = Bullet_Fire(start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed)
        elif type == "water":
            bullet = Bullet_Water(start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed)
        elif type == "electricity":
            bullet = Bullet_Electricity(start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed)
        elif type == "air":
            bullet = Bullet_Air(start_x, start_y, end_x, end_y, multiplier_scale, multiplier_damage, multiplier_speed)

        return bullet