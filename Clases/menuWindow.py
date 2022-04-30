import arcade
#import os
from Clases.Inventario import *

from Clases.Globals import *
from Clases.Protagonist import *
from Clases.Bullet import *
from Clases.escudo import *
from Clases.Setas import *
from Clases.mainWindow import *



class MenuWindow(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.enter_pressed = False

        self.option_hovered_on = 3

        self.timer = 0 #atributo de timer
        self.time_for_comparing = 0
        self.timer_for_collision = 0

    def setup(self):

        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):

        self.clear()
        arcade.start_render()

        if  self.option_hovered_on == 1:
            arcade.draw_rectangle_filled(240, 710, 350, 70, arcade.color.GRAY)
        if  self.option_hovered_on == 2:
            arcade.draw_rectangle_filled(240, 510, 350, 70, arcade.color.GRAY)
        if  self.option_hovered_on == 3:
            arcade.draw_rectangle_filled(240, 310, 350, 70, arcade.color.GRAY)
        arcade.draw_text("TEXT EXAMPLE 1", 100, 700, arcade.color.WHITE, 24)
        arcade.draw_text("TEXT EXAMPLE 2", 100, 500, arcade.color.WHITE, 24)
        arcade.draw_text("TEXT EXAMPLE 3", 100, 300, arcade.color.WHITE, 24)


    def on_update(self, delta_time):

        self.timer += delta_time
        if self.option_hovered_on > 3:
            self.option_hovered_on = 1
        if self.option_hovered_on < 1:
            self.option_hovered_on = 3
        if self.enter_pressed == True:
            if self.option_hovered_on == 1:
                self.window.show_view(mainWindow())
            if self.option_hovered_on == 2:
                self.window.show_view(mainWindow())
            if self.option_hovered_on == 3:
                self.window.show_view(mainWindow())


    def on_key_press(self, key, modifiers):

        if key == arcade.key.ENTER:
            self.enter_pressed = True
        elif key == arcade.key.W or key == arcade.key.UP:
            self.option_hovered_on -= 1
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.option_hovered_on += 1

        #Son solo para probar el tema de la vida (para eliminar)
        #elif key == arcade.key.Q:
            #self.protagonist.lose_life(5)
        #elif key == arcade.key.E:
            #self.protagonist.gain_life(5)


    def on_key_release(self, key, modifiers):

        if key == arcade.key.ENTER:
            self.enter_pressed = False


    #def on_mouse_press(self, x, y, button, modifiers):

        #bullet = self.protagonist.shoot(x, y)
        #self.bullet_list.append(bullet)


# def main():
#     window = MyWindow()
#     window.setup()
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()