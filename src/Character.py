import arcade

from src.Globals import *
from src.Bullet import *
from src.Armeria import *


class Character(arcade.Sprite):

    def __init__(self, scale, center_x, center_y, change_x, change_y):

        super().__init__(scale=scale)

        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.change_y = change_y

        self.movement_speed_normal = SPEED_PROTAGONIST
        self.movement_speed_now = SPEED_PROTAGONIST

        self.hp_max = HP_PROTAGONIST
        self.hp_now = HP_PROTAGONIST

        # Default to face-right
        self.face_direction = RIGHT_FACING
        # Used for flipping between image sequences
        self.cur_texture = 0

    def draw(self):

        super().draw()

        # self.print_life()

    def update(self):

        super().update()

    def update_animation(self, idle_textures, walk_textures, delta_time: float = 1 / 60, ):

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
        self.cur_texture += 1
        if self.cur_texture > (len(walk_textures) - 1) * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        direction = self.face_direction
        self.texture = self.walk_textures[frame][direction]

    def calculate_movement_speed(self, multiplier):
        if self.shift_pressed:
            multiplier *= 1.5
        if (self.up_pressed or self.down_pressed) and (self.left_pressed or self.right_pressed):
            multiplier *= 0.7071  # dividir por raiz de 2
        print(multiplier)
        return multiplier

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
        # Con lo que tenemos ahora mismo, en función de la vida maxima del personaje se imprime la barra.
        # Por lo que a más vida, la barra más grande. Y a menos vida, más pequeña.
        # Y si ponemos vidas diferentes, puede que quede raro

    def shoot(self, end_x, end_y, type):

        start_x = self.center_x
        start_y = self.center_y

        # Esto, obvio hay que hacerlo pillando el tipo de arma y los potenciadores que tenga el personaje
        multiplier_scale = 1
        multiplier_damage = 1
        multiplier_speed = 1

        bullet = Bullet(start_x, start_y, end_x, end_y, type, multiplier_scale, multiplier_damage, multiplier_speed)

        return bullet
