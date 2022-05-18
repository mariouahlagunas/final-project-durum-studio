import random
import math

from src.Character import *

class Enemy(Character):

    def __init__(self, center_x, center_y, change_x, change_y, objetive, map):
        super().__init__(SCALE_ENEMY, SPEED_ENEMY, HP_ENEMY, center_x, center_y, change_x, change_y)

        self.idle_textures = [arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_idle.png"),
                              arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_idle.png", flipped_horizontally=True)]

        self.walk_textures = []
        for i in range(NUM_WALK_TEXTURES_ENEMY):
            texture = [arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_walk{i}.png"),
                       arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_walk{i}.png", flipped_horizontally=True)]
            self.walk_textures.append(texture)

        self.attack_textures = []
        for i in range(NUM_ATTACK_TEXTURES_ENEMY):
            texture = [arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_climb{i}.png"),
                       arcade.load_texture(f"{TEXTURES_PATH_ENEMY}_climb{i}.png", flipped_horizontally=True)]
            self.attack_textures.append(texture)



        # Objetivo dinámico de nuestra IA
        self.objetive = objetive
        self.past_objetive_x = None
        self.past_objetive_y = None

        # Entorno estático de nuestra IA
        self.map = map

        # Variables de ataque
        self.time_for_shoot = random.randint(100, 300)


    def draw(self):
        super().draw()
        super().print_life()

        # if self.line_of_sight():
        #     arcade.draw_line(self.objetive.position[0], self.objetive.position[1], self.center_x, self.center_y,
        #                      arcade.color.RED, 2)



    def update(self):
        super().update()
        super().update_animation_walk(self.idle_textures, self.walk_textures)


    def updateIA(self, end_x, end_y):
        if self.distance() < 600:
            if self.line_of_sight():
                if self.time_for_shoot == 0:
                    self.time_for_shoot = random.randint(100, 100)
                    return self.attack_shoot(end_x, end_y)
                else:
                    self.time_for_shoot -= 1
            #else:
                # (IF) Si le he visto antes, voy a buscarle
                    # Aquí entra la última posición vista del objetivo
                # (ELSE) Si no le he visto, me pongo a patrullar
        #else:
            # Me pongo a patrullar


    def distance(self):
        return math.sqrt((self.position[0] - self.objetive.position[0]) ** 2 + (self.position[1] - self.objetive.position[1]) ** 2)


    def line_of_sight(self):
        if arcade.has_line_of_sight(self.position, self.objetive.position, self.map):
            return True
        else:
            return False


    def attack_shoot(self, end_x, end_y, timer_mouse=0):
        type = "electricity"
        multiplier_scale = 1
        multiplier_damage = 1
        multiplier_speed = 1

        bullet = super().shoot(end_x, end_y, type, timer_mouse, multiplier_scale, multiplier_damage, multiplier_speed)

        return bullet