import random

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



        # Entorno y objetivo de la IA
        self.map = map                  # Entorno estático por el que se va a mover
        self.objetive = objetive        # Objetivo dinámico

        # Parámetros configurables de la IA
        self.timer_update_IA = TIMER_FOR_UPDATE_IA
        self.range_of_action = DISTANCE_TO_ATTACK
        self.time_of_action = random.randint(TIME_FOR_SHOOT_MIN, TIME_FOR_SHOOT_MAX)

        # Parámetros para el funcionamiento de la IA
        self.objetive_seen = False
        self.can_action = False
        self.can_shoot = False
        self.path = None
        self.cur_position = None



    def draw(self):
        super().draw()
        super().print_life()


    def update(self, delta_time: float = 1 / 60):

        if self.timer_update_IA > 0:
            self.timer_update_IA -= delta_time
        else:
            self.timer_update_IA = TIMER_FOR_UPDATE_IA
            # self.timer_update_IA = 1
            self.IA()

        self.action()
        self.move()

        super().update()
        super().update_animation_walk(self.idle_textures, self.walk_textures)


    def IA(self):

        if self.distance() < self.range_of_action:

            if self.line_of_sight():

                if not self.can_action: self.can_action = True

                if not self.objetive_seen: self.objetive_seen = True

                # if self.path:
                #     self.path = None

            else:   # if not self.line_of_sight()

                if self.objetive_seen:
                    # if not self.path:
                    self.path = self.calculate_path(self.objetive.position)
                    self.cur_position = 0

                else:   # if not self.objetive_seen
                    if not self.path:
                        x = random.randint(self.position[0] - 200, self.position[0] + 200)
                        y = random.randint(self.position[1] - 200, self.position[1] + 200)
                        self.path = self.calculate_path((x, y))
                        self.cur_position = 0

                if self.can_action: self.can_action = False
                if self.objetive_seen: self.objetive_seen = False


        else:   # if not self.distance() < self.range_of_action
            if not self.path:
                x = random.randint(self.position[0] - 150, self.position[0] + 150)
                y = random.randint(self.position[1] - 150, self.position[1] + 150)
                self.path = self.calculate_path((x, y))
                self.cur_position = 0

            if self.can_action: self.can_action = False
            if self.objetive_seen: self.objetive_seen = False




    def distance(self):
        return math.sqrt((self.position[0] - self.objetive.position[0]) ** 2 + (self.position[1] - self.objetive.position[1]) ** 2)


    def line_of_sight(self):
        return arcade.has_line_of_sight(self.position, self.objetive.position, self.map)


    def calculate_path(self, position):
        barrier_list = arcade.AStarBarrierList(self, self.map, 128*0.5, 0 - 50, SCREEN_WIDTH + 50, 0 - 50, SCREEN_HEIGHT + 50)

        return arcade.astar_calculate_path(self.position, position, barrier_list, diagonal_movement = False)


    def move(self):
        if self.path:
            if self.cur_position < len(self.path):
                dest_x = self.path[self.cur_position][0]
                dest_y = self.path[self.cur_position][1]

                dif_x = dest_x - self.position[0]
                dif_y = dest_y - self.position[1]

                if dif_x > 0:
                    super().move_right()
                else:
                    super().move_left()
                if dif_y > 0:
                    super().move_up()
                else:
                    super().move_down()

                distance = math.sqrt((self.position[0] - dest_x) ** 2 + (self.position[1] - dest_y) ** 2)

                if distance <= SPEED_ENEMY:
                    self.cur_position += 1
            else:
                self.path = None
        else:
            super().not_move()


    # def action(self, delta_time: float = 1 / 60):
    #     pass

    # def action(self, delta_time: float = 1 / 60):
    #
    #     if self.can_action:
    #         if self.time_of_action > 0:
    #             self.time_of_action -= delta_time
    #         else:
    #             self.time_of_action = random.randint(TIME_FOR_SHOOT_MIN, TIME_FOR_SHOOT_MAX)
    #             self.can_shoot = True

    def action(self, delta_time: float = 1 / 60):
        if self.can_action:
            if self.time_of_action > 0:
                self.time_of_action -= delta_time
            else:
                self.time_of_action = random.randint(TIME_FOR_SHOOT_MIN, TIME_FOR_SHOOT_MAX)
                self.path = self.calculate_path(self.objetive.position)
                self.cur_position = 0


    def shoot(self, timer_mouse = 0):

        if self.can_shoot:

            self.can_shoot = False

            type = "electricity"
            multiplier_scale = 1
            multiplier_damage = 1
            multiplier_speed = 0.5

            bullet = super().shoot(self.objetive.position[0], self.objetive.position[1], type, timer_mouse, multiplier_scale, multiplier_damage, multiplier_speed)

            return bullet