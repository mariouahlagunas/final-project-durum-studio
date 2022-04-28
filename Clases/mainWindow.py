import arcade
from Inventario import *

from Globals import *
from Protagonist import *
from Bullet import *
from escudo import *
from Setas import *



class MyWindow(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.protagonist_list = None
        self.bullet_list = None

        self.protagonist = None
        self.Inventario = None
        self.escudo = None
        self.Setas = None


        # Track the current state of what key is pressed
        self.shift_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.speed_potion_activated = False

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.timer = 0 #atributo de timer
        self.time_for_comparing = 0


    def setup(self):

        arcade.set_background_color(arcade.color.BLACK)

        self.protagonist_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()


        self.protagonist = Protagonista(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0, 0)
        self.protagonist_list.append(self.protagonist)

        self.Inventario = inventario(2, 1)
        self.escudo = Escudo(1300, 41)
        self.Setas=setas(1350,41)

        #Carga de mapa

        #map_name = "mapa2/mapa2..tmx"
        #map_name = ":mapa2:/mapa2..tmx"

        #Terrenos
        #self.desert_layer = arcade.sprite_list()
        #self.camino_layer_1 = arcade.sprite_list(use_spatial_hash = True)
        #self.camino_layer_2 = arcade.sprite_list(use_spatial_hash = True)
        #self.camino_layer_3 = arcade.sprite_list(use_spatial_hash = True)
        #self.camino_layer_4 = arcade.sprite_list(use_spatial_hash = True)

        #desert_layer = "desierto3"
        #camino_layer_1 = "camino2"
        #camino_layer_2 = "camino2.1"
        #camino_layer_3 = "camino2.2"
        #camino_layer_4 = "camino2.3"

        #Colisiones

        #self.valla_layer = arcade.sprite_list(use_spatial_hash = True)
        #self.agua_layer = arcade.sprite_list(use_spatial_hash = True)
        #self.montanas_layer = arcade.sprite_list(use_spatial_hash = True)
        #self.arbol_layer = arcade.sprite_list(use_spatial_hash = True)
        #self.casa1_layer = arcade.sprite_list(use_spatial_hash = True)
        #self.casa2_layer = arcade.sprite_list(use_spatial_hash = True)

        #valla_layer = "valla"
        #agua_layer = "agua"
        #montanas_layer = "montañas"
        #arbol_layer = "arbol sin hojas"
        #casa1_layer = "casa1"
        #casa2_layer = "casa2"

        #Sprites

        #self.enemigo_sprite = arcade.sprite_list(use_spatial_hash = True)
        #self.npc1_sprite = arcade.sprite_list(use_spatial_hash = True)
        #self.npc2_sprite = arcade.sprite_list(use_spatial_hash = True)
        #self.npc3_sprite = arcade.sprite_list(use_spatial_hash = True)
        #self.me_sprite = arcade.sprite_list(use_spatial_hash = True)

        #enemigo_sprite = "enemigo"
        #npc1_sprite = "npc 1"
        #npc2_sprite = "npc 2"
        #npc3_sprite = "npc 3"
        #me_sprite = "yo"


        #my_map = arcade.tilemap.load_tilemap(map_name)

        #self.desert_layer = arcade.tilemap.process_layer(map_object = my_map, layer_name = desert_layer, scaling = 0.5, use_spatial_hash = True)
        #self.camino_layer_1 = arcade.tilemap.process_layer(map_object = my_map, layer_name = camino_layer_1, scaling = 0.5, use_spatial_hash = True)
        #self.camino_layer_2 = arcade.tilemap.process_layer(map_object = my_map, layer_name = camino_layer_2, scaling = 0.5, use_spatial_hash = True)
        #self.camino_layer_3 = arcade.tilemap.process_layer(map_object = my_map, layer_name = camino_layer_3, scaling = 0.5, use_spatial_hash = True)
        #self.camino_layer_4 = arcade.tilemap.process_layer(map_object = my_map, layer_name = camino_layer_4, scaling = 0.5, use_spatial_hash = True)
        #self.valla_layer = arcade.tilemap.process_layer(map_object = my_map, layer_name = valla_layer, scaling = 0.5, use_spatial_hash = True)
        #self.agua_layer = arcade.tilemap.process_layer(map_object = my_map, layer_name = agua_layer, scaling = 0.5, use_spatial_hash = True)
        #self.montanas_layer = arcade.tilemap.process_layer(map_object = my_map, layer_name = montanas_layer, scaling = 0.5, use_spatial_hash = True)
        #self.arbol_layer = arcade.tilemap.process_layer(map_object = my_map, layer_name = arbol_layer, scaling = 0.5, use_spatial_hash = True)
        #self.casa1_layer = arcade.tilemap.process_layer(map_object = my_map, layer_name = casa1_layer, scaling = 0.5, use_spatial_hash = True)
        #self.casa2_layer = arcade.tilemap.process_layer(map_object = my_map, layer_name = casa2_layer, scaling = 0.5, use_spatial_hash = True)
        #self.enemigo_sprite = arcade.tilemap.process_layer(map_object = my_map, layer_name = enemigo_sprite, scaling = 0.5, use_spatial_hash = True)
        #self.npc1_sprite = arcade.tilemap.process_layer(map_object = my_map, layer_name = npc1_sprite, scaling = 0.5, use_spatial_hash = True)
        #self.npc2_sprite = arcade.tilemap.process_layer(map_object = my_map, layer_name = npc2_sprite, scaling = 0.5, use_spatial_hash = True)
        #self.npc3_sprite = arcade.tilemap.process_layer(map_object = my_map, layer_name = npc3_sprite, scaling = 0.5, use_spatial_hash = True)
        #self.me_sprite = arcade.tilemap.process_layer(map_object = my_map, layer_name = me_sprite, scaling = 0.5, use_spatial_hash = True)

    def on_draw(self):

        self.clear()
        arcade.start_render()

        self.camera_for_sprites.use()

        self.protagonist.draw()
        self.bullet_list.draw()
        self.escudo.draw()
        self.Setas.draw()

        self.camera_for_gui.use()
        arcade.draw_text(f"Health:{self.protagonist.now_hp()} / {self.protagonist.max_hp()}", 10, 30, arcade.color.WHITE, 24)
        #Imprimimos en la pantalla los numeros de setas y escudos que hay encima del objeto
        arcade.draw_text(f"{self.Inventario.get_escudos()}", 1290, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.Inventario.get_setas()}", 1340, 30, arcade.color.WHITE, 24)


    def on_update(self, delta_time):

        self.timer += delta_time

        self.protagonist_list.update()
        self.bullet_list.update()

        for bullet in self.bullet_list:

            if bullet.bottom > self.height or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()

        if (self.timer - self.time_for_comparing) > 5:
            self.speed_potion_activated = False


    def on_key_press(self, key, modifiers):

        if key == arcade.key.LSHIFT:
            self.shift_pressed = True
            self.protagonist_movement()
        if key == arcade.key.A:
            self.left_pressed = True
            self.protagonist_movement()
        elif key == arcade.key.D:
            self.right_pressed = True
            self.protagonist_movement()
        elif key == arcade.key.W:
            self.up_pressed = True
            self.protagonist_movement()
        elif key == arcade.key.S:
            self.down_pressed = True
            self.protagonist_movement()
        elif key == arcade.key.Q:
            #Vemos si tenemos escudos en el inventario
            if self.Inventario.get_escudos()>0:
                #Si tiene, realiza su accion y encima se resta uno del inventario
                self.protagonist.gain_life(20)
                self.Inventario.set_escudo((self.Inventario.get_escudos())-1)
        elif key == arcade.key.E:
            self.speed_potion_activated = True
            ##Vemos si tenemos setas en el inventario
            if self.Inventario.get_setas() > 0:
                #Si tiene, realiza su accion y se gasta 1 en el inventario
                print(self.protagonist.movement_speed_now)
                self.protagonist.change_movement_speed(4)
                print(self.protagonist.movement_speed_now)
                self.Inventario.set_setas((self.Inventario.get_setas()) - 1)
                self.time_for_comparing = self.timer


        #Son solo para probar el tema de la vida (para eliminar)
        #elif key == arcade.key.Q:
            #self.protagonist.lose_life(5)
        #elif key == arcade.key.E:
            #self.protagonist.gain_life(5)


    def on_key_release(self, key, modifiers):

        if key == arcade.key.LSHIFT:
            self.shift_pressed = False
            self.protagonist_movement()
        if key == arcade.key.W:
            self.up_pressed = False
            self.protagonist_movement()
        elif key == arcade.key.S:
            self.down_pressed = False
            self.protagonist_movement()
        elif key == arcade.key.A:
            self.left_pressed = False
            self.protagonist_movement()
        elif key == arcade.key.D:
            self.right_pressed = False
            self.protagonist_movement()


    def on_mouse_press(self, x, y, button, modifiers):

        bullet = self.protagonist.shoot(x, y)
        self.bullet_list.append(bullet)


    def protagonist_movement(self):

        if self.shift_pressed:
            self.protagonist.change_movement_speed(1.5)
        else:
            if not self.speed_potion_activated:
                self.protagonist.change_movement_speed(1)

        self.protagonist.not_move()
        if self.up_pressed and not self.down_pressed:
            self.protagonist.move_up()
        elif self.down_pressed and not self.up_pressed:
            self.protagonist.move_down()
        if self.left_pressed and not self.right_pressed:
            self.protagonist.move_left()
        elif self.right_pressed and not self.left_pressed:
            self.protagonist.move_right()


def main():
    window = MyWindow()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()