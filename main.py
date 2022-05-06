import arcade

from src.mainWindow import *


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    #start_view = MenuScreen()
    start_view = MainGame()
    window.show_view(start_view)
    arcade.run()


if __name__ == '__main__':
    main()