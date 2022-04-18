import random
import arcade

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
                         start_x=80 + HEALTH_NUMBER_OFFSET_X,
                         start_y=602 + HEALTH_NUMBER_OFFSET_Y,
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

        arcade.draw_rectangle_filled(center_x=62- 0.5 * (HEALTHBAR_WIDTH - health_width),
                                     center_y=576 - 10,
                                     width=health_width+30,
                                     height=HEALTHBAR_HEIGHT,
                                     color=arcade.color.GREEN)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit4.wav")
        self.death_sound = arcade.load_sound(":resources:sounds/hit5.wav")

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = ""

        # Image from kenney.nl
        self.player_sprite = SpriteWithHealth(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING_PLAYER,max_health=100)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)


        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = SpriteWithHealth(":resources:images/items/coinGold.png",
                                    SPRITE_SCALING_COIN,
                                    max_health=5)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(150, SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.coin_list.draw()
        self.player_list.draw()
        for player in self.player_list:
            player.draw_health_number()
            player.draw_health_bar()



        # Render the text
        arcade.draw_text(f"Health: {self.score}", 10, 575, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
    def on_update(self, delta_time):

        # Loop through each bullet
        for coin in self.coin_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(coin, self.player_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                coin.remove_from_sprite_lists()

            # For every coin we hit, process
            for player in hit_list:
                # Make sure this is the right type of class
                if not isinstance(player, SpriteWithHealth):
                    raise TypeError("List contents must be all ints")

                # Remove one health point
                player.cur_health += 20

                # Check health
                if player.cur_health <= 0:
                    # Dead
                    player.remove_from_sprite_lists()
                    self.score += 1
                    arcade.play_sound(self.death_sound)
                else:
                    # Not dead
                    arcade.play_sound(self.hit_sound)



def main():
    """ Main Program """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()