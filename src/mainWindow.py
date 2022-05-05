import arcade

from src.Globals import *
from src.Protagonist import *
from src.Bullet import *
from src.Inventario import *
from src.escudo import *
from src.Setas import *
from src.Armeria import *
from src.Bullet_Inventario import *


class MenuScreen(arcade.View):

    def __init__(self):

        super().__init__()

        self.enter_pressed = False

        self.option_hovered_on = 1

        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):

        self.clear()
        arcade.start_render()

        if  self.option_hovered_on == 1:
            arcade.draw_rectangle_filled(280, 710, 420, 70, arcade.color.GRAY)
            arcade.draw_circle_filled(90, 710, 6, arcade.color.WHITE)
        if  self.option_hovered_on == 2:
            arcade.draw_rectangle_filled(280, 510, 420, 70, arcade.color.GRAY)
            arcade.draw_circle_filled(90, 510, 6, arcade.color.WHITE)
        if  self.option_hovered_on == 3:
            arcade.draw_rectangle_filled(280, 310, 420, 70, arcade.color.GRAY)
            arcade.draw_circle_filled(90, 310, 6, arcade.color.WHITE)
        arcade.draw_text("Jugar", 100, 700, arcade.color.WHITE, 24)
        arcade.draw_text("Jugar pero en otra línea", 100, 500, arcade.color.WHITE, 24)
        arcade.draw_text("Salir del juego", 100, 300, arcade.color.WHITE, 24)


    def on_update(self, delta_time):

        if self.option_hovered_on > 3:
            self.option_hovered_on = 1
        if self.option_hovered_on < 1:
            self.option_hovered_on = 3
        if self.enter_pressed == True:
            if self.option_hovered_on == 1:
                self.window.show_view(MainGame())
            if self.option_hovered_on == 2:
                self.window.show_view(MainGame())
            if self.option_hovered_on == 3:
                self.window.close()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.ENTER:
            self.enter_pressed = True
        elif key == arcade.key.W or key == arcade.key.UP:
            self.option_hovered_on -= 1
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.option_hovered_on += 1


    def on_key_release(self, key, modifiers):

        if key == arcade.key.ENTER:
            self.enter_pressed = False


class MainGame(arcade.View):

    def __init__(self):

        super().__init__()

        self.protagonist_list = None
        self.enemies_list = None
        self.bullet_list = None

        self.protagonist = None
        self.Inventario = None
        self.escudo = None
        self.Setas = None
        self.Bullet_fire = None
        self.Bullet_water = None
        self.FIREBULLET_INV= None
        self.WATERBULLET_INV = None

        #self.physics_engine = None # no se usará por ahora esto debido a los distintos cambios que he comentado sobre las colisiones, esto se usará probablemente para paredes.

        # Track the current state of what key is pressed
        self.shift_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.Type = ""

        self.speed_potion_activated = False

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.timer = 0 #atributo de timer
        self.time_for_comparing = 0
        self.timer_for_collision = 0

    def on_show(self):
        self.setup()

    def setup(self):
        # Cargamos el mapa generado con Tiled Map
        self.tile_map = arcade.load_tilemap(map_file=MAP_NAME, scaling= MAP_SCALE, layer_options=MAP_LAYER_OPTIONS)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Inicializamos las listas de Sprites
        self.protagonist_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Cargamos a nuestro protagonista en la escena
        self.protagonist = Protagonista(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0, 0)
        self.protagonist_list.append(self.protagonist)

        # Cargamos a los enemigos en la escena
        for position_enemie in self.scene["edna"]:
            enemie = Protagonista(position_enemie.center_x, position_enemie.center_y, 0, 0)
            self.enemies_list.append(enemie)

        # COSITAS SOBRE LAS BALAS Y EL INVENTARIO QUE TENGO QUE MIRAR
        self.FIREBULLET_INV = Bullet_num("rojo", 1145, 41)
        self.WATERBULLET_INV = Bullet_num("azul", 1195, 41)
        self.WATERBULLET_INV.angle = 90
        self.Inventario = inventario(2, 1, 30, 30)
        self.escudo = Escudo(1300, 41)
        self.Setas=setas(1350,41)


    def on_draw(self):
        self.clear()
        arcade.start_render()

        # Imprimimos el contenido del videojuego.
        self.camera_for_sprites.use()

        self.scene.draw()

        for protagonist in self.protagonist_list:
            protagonist.draw()
        for enemie in self.enemies_list:
            enemie.draw()
        for bullet in self.bullet_list:
            bullet.draw()


        self.escudo.draw()
        self.Setas.draw()
        self.FIREBULLET_INV.draw()
        self.WATERBULLET_INV.draw()

        # Imprimimos la GUI del videojuego
        self.camera_for_gui.use()
        arcade.draw_text(f"Health:{self.protagonist.now_hp()} / {self.protagonist.max_hp()}", 10, 30, arcade.color.WHITE, 24)
        #Imprimimos en la pantalla los numeros de setas y escudos que hay encima del objeto
        arcade.draw_text(f"{self.Inventario.get_escudos()}", 1290, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.Inventario.get_setas()}", 1340, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.Inventario.get_water()}", 1200, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.Inventario.get_fire()}", 1150, 30, arcade.color.WHITE, 24)


    def on_update(self, delta_time):

        self.timer += delta_time




        self.protagonist_list.update()
        self.enemies_list.update()
        self.bullet_list.update()

        for bullet in self.bullet_list:
            # Si la bala sale de los margenes de la pantalla la eliminamos
            if bullet.bottom > SCREEN_HEIGHT or bullet.top < 0 or bullet.right < 0 or bullet.left > SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

            # Si la bala cocha contra un obstáculo del entorno la borramos
            bullet_hit_env_list = arcade.check_for_collision_with_list(bullet, self.scene["cajas"])
            if len(bullet_hit_env_list) > 0:
                bullet.remove_from_sprite_lists()

            # Si una bala cocha contra un enemigo del entorno la borramos y le quitamos vida al personaje
            bullet_hit_enemie_list = arcade.check_for_collision_with_list(bullet, self.enemies_list)
            if len(bullet_hit_enemie_list) > 0:
                bullet.remove_from_sprite_lists()
            for enemie in bullet_hit_enemie_list:
                enemie.lose_life(bullet.get_damage())
                # if enemie.alive():
                #     enemie.remove_from_sprite_list()












        if (self.timer - self.time_for_comparing) > 5:
            self.speed_potion_activated = False


        if len(self.scene["edna"]) == 0:
            game_view = GameOverWindow()
            self.window.show_view(game_view)

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
        if key == arcade.key.R:
            self.Type = "agua"
        if key == arcade.key.T:
            self.Type = "fuego"
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
                self.protagonist.change_movement_speed(2.5)
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
        # Mirar con que arma se está disparando
        # Mirar potenciadores que pueda tener el personaje
        # Mirar si hay munición de esa arma en el inventario
        Armeria = Armas(self.Type)
        if Armeria.get_arma() == "fuego":
            type = "fire"
            if self.Inventario.get_fire() > 0:
                self.Inventario.set_fire((self.Inventario.get_fire()) - 1)
                bullet = self.protagonist.shoot(x, y, type)
                self.bullet_list.append(bullet)

            else:
                print("No hay municion de esta arma")
        if Armeria.get_arma() == "agua":
            type = "water"
            if self.Inventario.get_water() > 0:
                self.Inventario.set_water((self.Inventario.get_water()) - 1)
                bullet = self.protagonist.shoot(x, y, type)
                self.bullet_list.append(bullet)

            else:
                print("No hay municion de esta arma")


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


class GameOverWindow(arcade.View):

    def __init__(self):

        super().__init__()

        self.enter_pressed = False

        self.option_hovered_on = 1

        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):

        self.clear()
        arcade.start_render()

        if  self.option_hovered_on == 1:
            arcade.draw_rectangle_filled(645, 310, 100, 50, arcade.color.GRAY)
        if  self.option_hovered_on == 2:
            arcade.draw_rectangle_filled(755, 310, 100, 50, arcade.color.GRAY)
        if  self.option_hovered_on == 3:
            arcade.draw_rectangle_filled(700, 210, 200, 50, arcade.color.GRAY)
        arcade.draw_text("GAME OVER", 340, 600, arcade.color.WHITE, 80)
        arcade.draw_text("RETRY?", 590, 500, arcade.color.WHITE, 40)
        arcade.draw_text("YES", 610, 300, arcade.color.WHITE, 24)
        arcade.draw_text("NO", 730, 300, arcade.color.WHITE, 24)
        arcade.draw_text("MAIN MENU", 605, 200, arcade.color.WHITE, 24)

    def on_update(self, delta_time):

        #if self.option_hovered_on > 2:
        #    self.option_hovered_on = 1
        #if self.option_hovered_on < 1:
        #    self.option_hovered_on = 2
        if self.enter_pressed == True:
            if self.option_hovered_on == 1:
                self.window.show_view(MainGame())
            if self.option_hovered_on == 2:
                self.window.close()
            if self.option_hovered_on == 3:
                self.window.show_view(MenuScreen())


    def on_key_press(self, key, modifiers):

        if key == arcade.key.ENTER:
            self.enter_pressed = True
        elif (key == arcade.key.A or key == arcade.key.LEFT) and (self.option_hovered_on == 1):
            self.option_hovered_on = 2
        elif (key == arcade.key.D or key == arcade.key.RIGHT) and (self.option_hovered_on == 1):
            self.option_hovered_on = 2
        elif (key == arcade.key.A or key == arcade.key.LEFT) and (self.option_hovered_on == 2):
            self.option_hovered_on = 1
        elif (key == arcade.key.D or key == arcade.key.RIGHT) and (self.option_hovered_on == 2):
            self.option_hovered_on = 1
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.option_hovered_on = 3
        elif key == arcade.key.W or key == arcade.key.UP:
            self.option_hovered_on = 1

    def on_key_release(self, key, modifiers):

        if key == arcade.key.ENTER:
            self.enter_pressed = False