import random
import arcade
import main

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.6
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Hit Points and Health Bars "

BULLET_SPEED = 5

HEALTHBAR_WIDTH = 25
HEALTHBAR_HEIGHT = 3
HEALTHBAR_OFFSET_Y = -10

HEALTH_NUMBER_OFFSET_X = -10
HEALTH_NUMBER_OFFSET_Y = -25


class SpriteWithHealth(arcade.Sprite):
    """ Sprite with hit points """

    def __init__(self, image, scale, max_health):
        super().__init__(image, scale)

        # Add extra attributes for health
        self.max_health = max_health
        self.cur_health = max_health

    def draw_health_number(self):
        """ Draw how many hit points we have """

        health_string = f"{self.cur_health}/{self.max_health}"
        arcade.draw_text(health_string,
                         start_x=73 + HEALTH_NUMBER_OFFSET_X,
                         start_y=45 + HEALTH_NUMBER_OFFSET_Y,
                         font_size=12,
                         color=arcade.color.WHITE)

    def draw_health_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.cur_health < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y + HEALTHBAR_OFFSET_Y,
                                         width=HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.RED)

        # Calculate width based on health
        health_width = HEALTHBAR_WIDTH * (self.cur_health / self.max_health)

        arcade.draw_rectangle_filled(center_x=65- 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=20 - 10,
                                     width=health_width+30,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)


class MyGame(arcade.Window):
    """ Main application class. """


    def setup(self):
        self.score =""


    def on_draw(self):
        self.personaje_principal.draw_health_number()
        self.personaje_principal.draw_health_bar()

        arcade.draw_text(f"Health: {self.score}", 10, 20, arcade.color.WHITE, 14)

