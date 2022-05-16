import arcade

from src.Character import *
from src.Inventario import *
from src.Gemas import *


class Protagonist(Character):

    def __init__(self, center_x, center_y, change_x, change_y):
        super().__init__(SCALE_PROTAGONIST, SPEED_PROTAGONIST, HP_PROTAGONIST, center_x, center_y, change_x, change_y)

        self.idle_textures = [arcade.load_texture(f"{TEXTURES_PATH_PROTAGONIST}_idle.png"),
                              arcade.load_texture(f"{TEXTURES_PATH_PROTAGONIST}_idle.png", flipped_horizontally=True)]

        self.walk_textures = []
        for i in range(NUM_WALK_TEXTURES_PROTAGONIST):
            texture = [arcade.load_texture(f"{TEXTURES_PATH_PROTAGONIST}_walk{i}.png"),
                       arcade.load_texture(f"{TEXTURES_PATH_PROTAGONIST}_walk{i}.png", flipped_horizontally=True)]
            self.walk_textures.append(texture)

        self.attack_textures = []
        for i in range(NUM_ATTACK_TEXTURES_PROTAGONIST):
            texture = [arcade.load_texture(f"{TEXTURES_PATH_PROTAGONIST}_climb{i}.png"),
                       arcade.load_texture(f"{TEXTURES_PATH_PROTAGONIST}_climb{i}.png", flipped_horizontally=True)]
            self.attack_textures.append(texture)

        self.shift_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def draw(self):
        super().draw()
    def set_up(self):
        self.Inventario = inventario(2, 2, 30, 30, 30, 30, 100)
        self.gemas=Gemas(3,3)

    def update(self):
        super().update()

        multiplier_speed = self.calculate_movement_speed()
        super().change_movement_speed(multiplier_speed)

        self.not_move()
        if self.up_pressed and not self.down_pressed:
            self.move_up()
        elif self.down_pressed and not self.up_pressed:
            self.move_down()
        if self.left_pressed and not self.right_pressed:
            self.move_left()
        elif self.right_pressed and not self.left_pressed:
            self.move_right()

        super().update_animation_walk(self.idle_textures, self.walk_textures)
        super().update_animation_attack(self.attack_textures)

    def calculate_movement_speed(self, multiplier=1):
        if self.shift_pressed:
            multiplier *= 1.5

        if (xor(self.up_pressed, self.down_pressed)) and (xor(self.left_pressed, self.right_pressed)):
            # Dividir por raiz de 2
            multiplier *= 0.7071

        return multiplier

    def want_run(self, pressed):
        if pressed:
            self.shift_pressed = True
        else:
            self.shift_pressed = False

    def want_move_up(self, pressed):
        if pressed:
            self.up_pressed = True
        else:
            self.up_pressed = False

    def want_move_down(self, pressed):
        if pressed:
            self.down_pressed = True
        else:
            self.down_pressed = False

    def want_move_left(self, pressed):
        if pressed:
            self.left_pressed = True
        else:
            self.left_pressed = False

    def want_move_right(self, pressed):
        if pressed:
            self.right_pressed = True
        else:
            self.right_pressed = False

    def shoot(self, type, end_x, end_y, timer_mouse=0):
        # El parametro se borra y se saca del arma que lleve, pero estoy en pruebas
        # type = "electricity"
        multiplier_scale = 1
        multiplier_damage = 1
        multiplier_speed = 1

        bullet = super().shoot(end_x, end_y, type, timer_mouse, multiplier_scale, multiplier_damage, multiplier_speed)

        return bullet