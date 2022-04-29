import arcade
#import os
from Clases.Inventario import *

from Clases.Globals import *
from Clases.Protagonist import *
from Clases.Bullet import *
from Clases.escudo import *
from Clases.Setas import *



class MyWindow(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        #file_path = os.path.dirname(os.path.abspath(__file__))
        #os.chdir(file_path)

        self.protagonist_list = None
        self.bullet_list = None

        self.protagonist = None
        self.Inventario = None
        self.escudo = None
        self.Setas = None

        #self.physics_engine = None # no se usará por ahora esto debido a los distintos cambios que he comentado sobre las colisiones, esto se usará probablemente para paredes.

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
        self.timer_for_collision = 0

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
        #map_name = "assets/tilemaps/pruebaMapa/mapa.tmx"
        map_name = "assets/tilemaps/pruebaMapa2/mapa.tmx"

        #Creamos el mapa

        layer_options = {
            "suelo":{
                "use_spatial_hash": True
            },
            "cajas":{
                "use_spatial_hash": True,
            },
            "edna":{
                "use_spatial_hash": True,
            },
        }
        my_map = arcade.load_tilemap(map_name,1,layer_options)
        self.scene = arcade.Scene.from_tilemap(my_map)

        #self.physics_engine = arcade.PhysicsEngineSimple(self.protagonist,self.scene["cajas"]) # no se usará por ahora esto debido a los distintos cambios que he comentado sobre las colisiones, esto se usará probablemente para paredes.


    def on_draw(self):

        self.clear()
        arcade.start_render()

        self.camera_for_sprites.use()

        self.scene.draw()
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


        #self.physics_engine.update() # no se usará por ahora esto debido a los distintos cambios que he comentado sobre las colisiones, esto se usará probablemente para paredes.
        edna_hit_list = arcade.check_for_collision_with_list(self.protagonist,self.scene["edna"])

        # PARA PRUEBAS. cada vez que se interactua con edna se imprime la ubicación de donde está esa edna
        for edna in edna_hit_list:
            print ("(",edna.center_x,",",edna.center_y,")")

        # Cuando se dispara a edna, edna y la bala desaparecen
        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.scene["edna"])
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
            for edna in hit_list:
                edna.remove_from_sprite_lists()
                print ("edna is hit")

            # Cuando tengamos nivels con paredes miraremos si la bala choca con la pared y si lo hace desaparece
            #if bullet.bottom > SCREEN_HEIGHT:
            #    bullet.remove_from_sprite_lists()

        box_hit_list = arcade.check_for_collision_with_list(self.protagonist,self.scene["cajas"])

        #Se añadió esto debido a las siguientes razones:
        #1.El sistema anterior de:
        #       self.physics_engine = arcade.PhysicsEngineSimple(self.protagonist,self.scene["cajas"])
        #solo funciona con paredes, no se puede añadir más objetes con el que el personaje se choca, esto es según la documentación de arcade, si intentas hacer lo siguiente da errores:
        #       self.physics_engine = arcade.PhysicsEngineSimple(self.protagonist,self.scene["cajas"])
        #       self.physics_engine = arcade.PhysicsEngineSimple(self.protagonist,self.scene["edna"])
        #y también esto dará errores:
        #       #self.physics_engine = arcade.PhysicsEngineSimple(self.protagonist,self.scene["cajas"],self.scene["edna"])
        #ya que, como he dicho antes, esto es solo para que el personaje no se choque con los que son los paredes del nivel, se podrá utilizar en un futuro con lo que serán las paredes de las habitaciones
        for collision in box_hit_list:
            if self.scene["cajas"] in collision.sprite_lists:
                print ("box")
                #collision.remove_from_sprite_lists()
                self.protagonist.not_move()
                if self.up_pressed:
                    self.protagonist.center_y = self.protagonist.center_y - 10
                if self.down_pressed:
                    self.protagonist.center_y = self.protagonist.center_y + 10
                if self.left_pressed:
                    self.protagonist.center_x = self.protagonist.center_x + 10
                if self.right_pressed:
                    self.protagonist.center_x = self.protagonist.center_x - 10


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
                self.protagonist.change_movement_speed(2)
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
            self.protagonist.change_movement_speed(1)
        else:
            if not self.speed_potion_activated:
                self.protagonist.change_movement_speed(0.5)

        self.protagonist.not_move()
        if self.up_pressed and not self.down_pressed:
            self.protagonist.move_up()
        elif self.down_pressed and not self.up_pressed:
            self.protagonist.move_down()
        if self.left_pressed and not self.right_pressed:
            self.protagonist.move_left()
        elif self.right_pressed and not self.left_pressed:
            self.protagonist.move_right()


# def main():
#     window = MyWindow()
#     window.setup()
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()