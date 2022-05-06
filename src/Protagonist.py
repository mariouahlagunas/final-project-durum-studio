import arcade

from src.Character import *


class Protagonist(Character):

    def __init__(self, center_x, center_y, change_x, change_y):

        super().__init__(SCALE_PROTAGONIST, center_x, center_y, change_x, change_y)

        self.shift_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        texture_path = ":resources:images/animated_characters/male_person/malePerson"

        self.idle_textures = [arcade.load_texture(f"{texture_path}_idle.png"),
                              arcade.load_texture(f"{texture_path}_idle.png", flipped_horizontally=True)]

        self.walk_textures = []
        for i in range(8):
            texture = [arcade.load_texture(f"{texture_path}_walk{i}.png"),
                       arcade.load_texture(f"{texture_path}_walk{i}.png", flipped_horizontally=True)]
            self.walk_textures.append(texture)

    def draw(self):

        super().draw()

    def update(self):

        super().update()
        self.change_movement_speed(self.calculate_movement_speed(1))
        self.not_move()
        if self.up_pressed and not self.down_pressed:
            self.move_up()
        elif self.down_pressed and not self.up_pressed:
            self.move_down()
        if self.left_pressed and not self.right_pressed:
            self.move_left()
        elif self.right_pressed and not self.left_pressed:
            self.move_right()

        super().update_animation(self.idle_textures, self.walk_textures)

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
