import arcade
import random
import arcade.gui

from src.Globals import *
from src.Character import *
from src.Protagonist import *
from src.Enemy import *
from src.Bullet import *
from src.Inventario import *
from src.escudo import *
from src.Setas import *
from src.Armeria import *
from src.Bullet_Inventario import *
from src.Bullet_Fire import *

from src.Mascota import *  # arreglar por favor


class MenuScreen(arcade.View):

    def __init__(self):

        super().__init__()

        self.enter_pressed = False

        self.option_hovered_on = 1

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        self.clear()
        arcade.start_render()

        if self.option_hovered_on == 1:
            arcade.draw_rectangle_filled(280, 710, 420, 70, arcade.color.GRAY)
            arcade.draw_circle_filled(90, 710, 6, arcade.color.WHITE)
        if self.option_hovered_on == 2:
            arcade.draw_rectangle_filled(280, 510, 420, 70, arcade.color.GRAY)
            arcade.draw_circle_filled(90, 510, 6, arcade.color.WHITE)
        if self.option_hovered_on == 3:
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


class Inventory(arcade.View):
    def __init__(self):

        super().__init__()
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()

        # Creating Button using UIFlatButton
        air_bullet = arcade.gui.UIFlatButton(text="20",
                                             width=40)
        water_bullet = arcade.gui.UIFlatButton(text="20",
                                               width=40)
        fire_bullet = arcade.gui.UIFlatButton(text="20",
                                              width=40)
        electricity_bullet = arcade.gui.UIFlatButton(text="20",
                                                     width=40)

        # Adding button in our uimanager
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                align_x=167,
                align_y=310,
                anchor_x="left",
                child=air_bullet)
        )
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                align_x=217,
                align_y=310,
                anchor_x="left",
                child=electricity_bullet)
        )
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                align_x=267,
                align_y=310,
                anchor_x="left",
                child=fire_bullet)
        )
        self.uimanager.add(
            arcade.gui.UIAnchorWidget(
                align_x=322,
                align_y=310,
                anchor_x="left",
                child=water_bullet)
        )

        @air_bullet.event("on_click")
        def on_click_air_bullet(event):
            self.purchase_air_bullet() \
 \
            @ water_bullet.event("on_click")

        def on_click_water_bullet(event):
            self.purchase_water_bullet()

        @fire_bullet.event("on_click")
        def on_click_fire_bullet(event):
            self.purchase_fire_bullet()

        @electricity_bullet.event("on_click")
        def on_click_electricity_bullet(event):
            self.purchase_electricity_bullet()

        self.protagonist_list = None
        self.enemies_list = None
        self.bullet_list = None
        self.gema_roja = None
        self.gema_azul = None
        self.protagonist = None
        self.escudo = None
        self.Setas = None
        self.money_imagen = None
        self.Bullet_fire = None
        self.Bullet_water = None
        self.FIREBULLET_INV = None
        self.WATERBULLET_INV = None
        self.type_bullet = "electricity"  # Para pruebas, cuando las acabe lo borro

        self.Type = ""

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def on_show(self):
        self.setup()

    def setup(self):

        arcade.set_background_color(arcade.color.SKY_BLUE)
        # Cargamos a nuestro protagonista en la escena
        self.protagonist = Protagonist(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0, 0)

        # COSITAS SOBRE LAS BALAS Y EL INVENTARIO QUE TENGO QUE MIRAR
        self.FIREBULLET_INV = Bullet_num("rojo", 268, 759)
        self.WATERBULLET_INV = Bullet_num("azul", 320, 759)
        self.WATERBULLET_INV.angle = 90
        self.gema_roja = Bullet_num("gema_azul", 1300, 708)
        self.gema_azul = Bullet_num("gema_roja", 1300, 658)
        self.escudo = Escudo(397, 760)
        self.money_imagen = Escudo(1300, 760)
        self.Setas = setas(456, 758)
        self.protagonist.set_up()

        # self.physics_engine = arcade.PhysicsEngineSimple(self.protagonist,self.scene["cajas"]) # no se usará por ahora esto debido a los distintos cambios que he comentado sobre las colisiones, esto se usará probablemente para paredes.

    def on_key_press(self, key, modifiers):
        if key == arcade.key.I:
            self.window.show_view(MainGame())
        if key == arcade.key.B:
            self.purchase_air_bullet()

    def purchase_air_bullet(self):
        if self.protagonist.Inventario.get_money() >= 20:
            self.protagonist.Inventario.set_money(self.protagonist.Inventario.get_money() - 20)
            self.protagonist.Inventario.set_Air(self.protagonist.Inventario.get_Air() + 10)

    def purchase_water_bullet(self):
        if self.protagonist.Inventario.get_money() >= 20:
            self.protagonist.Inventario.set_money(self.protagonist.Inventario.get_money() - 20)
            self.protagonist.Inventario.set_water(self.protagonist.Inventario.get_water() + 10)

    def purchase_fire_bullet(self):
        if self.protagonist.Inventario.get_money() >= 20:
            self.protagonist.Inventario.set_money(self.protagonist.Inventario.get_money() - 20)
            self.protagonist.Inventario.set_fire(self.protagonist.Inventario.get_fire() + 10)

    def purchase_electricity_bullet(self):
        if self.protagonist.Inventario.get_money() >= 20:
            self.protagonist.Inventario.set_money(self.protagonist.Inventario.get_money() - 20)
            self.protagonist.Inventario.set_electricity(self.protagonist.Inventario.get_electricity() + 10)

    def on_draw(self):
        self.clear()
        arcade.start_render()

        # Imprimimos el contenido del videojuego.
        self.camera_for_sprites.use()
        self.uimanager.draw()

        arcade.draw_rectangle_filled(187, 760, 50, 40, arcade.color.BLUE)
        arcade.draw_rectangle_filled(237, 760, 50, 40, arcade.color.BLUE)
        arcade.draw_rectangle_filled(284, 760, 50, 40, arcade.color.BLUE)
        arcade.draw_rectangle_filled(334, 760, 50, 40, arcade.color.BLUE)
        arcade.draw_rectangle_filled(334, 760, 300, 40, arcade.color.BLUE)

        arcade.draw_rectangle_filled(322, 780, 324, 4, arcade.color.WHITE)
        arcade.draw_rectangle_filled(322, 740, 324, 4, arcade.color.WHITE)
        arcade.draw_rectangle_filled(485, 760, 5, 40, arcade.color.WHITE)
        arcade.draw_rectangle_filled(162, 760, 5, 40, arcade.color.WHITE)
        arcade.draw_rectangle_filled(212, 760, 5, 40, arcade.color.WHITE)
        arcade.draw_rectangle_filled(262, 760, 5, 40, arcade.color.WHITE)
        arcade.draw_rectangle_filled(312, 760, 5, 40, arcade.color.WHITE)
        arcade.draw_rectangle_filled(369, 760, 5, 40, arcade.color.WHITE)
        arcade.draw_rectangle_filled(425, 760, 5, 40, arcade.color.WHITE)

        self.escudo.draw()
        self.money_imagen.draw()
        self.Setas.draw()
        self.FIREBULLET_INV.draw()
        self.WATERBULLET_INV.draw()
        self.gema_roja.draw()
        self.gema_azul.draw()

        # Imprimimos la GUI del videojuego
        self.camera_for_gui.use()
        arcade.draw_text(f"{self.protagonist.Inventario.get_escudos()}", 448, 750, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_setas()}", 388, 750, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_water()}", 323, 750, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_fire()}", 273, 750, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_electricity()}", 218, 750, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_Air()}", 168, 750, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_money()}", 1320, 750, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.gemas.get_velocidad()}", 1327, 648, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.gemas.get_tamaño()}", 1327, 698, arcade.color.WHITE, 24)


class MainGame(arcade.View):

    def __init__(self):

        super().__init__()

        self.protagonist_list = None
        self.enemies_list = None
        self.bullet_list = None
        self.bullet_enemy_list = None
        self.mascota_list = None

        self.barrier_list = None
        self.path = None
        self.mascota = None
        self.protagonist = None
        self.escudo = None
        self.Setas = None
        self.money_imagen = None
        self.Bullet_fire = None
        self.Bullet_water = None
        self.FIREBULLET_INV = None
        self.WATERBULLET_INV = None
        self.type_bullet = "electricity"  # Para pruebas, cuando las acabe lo borro
        self.timer_mouse = 0
        self.gema_roja = None
        self.gema_azul = None

        self.physics_engine = None  # no se usará por ahora esto debido a los distintos cambios que he comentado sobre las colisiones, esto se usará probablemente para paredes.

        # Track the current state of what key is pressed

        self.Type = ""

        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.timer = 0  # atributo de timer
        self.timer_for_collision = 0

    def on_show(self):
        self.setup()

    def setup(self):
        # Cargamos el mapa generado con Tiled Map
        self.tile_map = arcade.load_tilemap(map_file=MAP_PATH, scaling=MAP_SCALE, layer_options=MAP_LAYER_OPTIONS)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Inicializamos las listas de Sprites
        self.protagonist_list = arcade.SpriteList()
        self.enemies_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.bullet_enemy_list = arcade.SpriteList()
        self.mascota_list = arcade.SpriteList()

        # Cargamos a nuestro protagonista en la escena
        self.protagonist = Protagonist(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0, 0)
        # self.protagonist = Protagonist(450, 650, 0, 0)
        self.protagonist_list.append(self.protagonist)
        # Cargamos a nuestro mascota en la escena
        self.mascota = Mascota(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0, 0, self.protagonist, self.scene["cajas"])
        self.mascota_list.append(self.mascota)

        # Cargamos a los enemigos en la escena
        enemies = self.scene["enemigos"]
        num_enemies = 0
        if DIFFICULTY == "easy":
            num_enemies = 1
            # num_enemies = int(len(enemies) * (1/3))
        elif DIFFICULTY == "normal":
            num_enemies = int(len(enemies) * (1 / 2))
        else:  # DIFFICULTY == "hard"
            num_enemies = int(len(enemies) * (2 / 3))
        # Simulamos la tirada de un dado, en caso de que salga 10,11o12 añadimos un enemigo más
        # if random.randint(1, 12) > 9:
        #     num_enemies += 1

        for i in range(num_enemies):
            selected = enemies.pop(random.randint(0, len(enemies) - 1))
            enemy = Enemy(selected.center_x, selected.center_y, 0, 0, self.protagonist, self.scene["cajas"])
            # enemy = Enemy(selected.center_x, selected.center_y, 0, 0, self.protagonist, self.scene["colisiones"])
            self.enemies_list.append(enemy)

        # COSITAS SOBRE LAS BALAS Y EL INVENTARIO QUE TENGO QUE MIRAR
        self.FIREBULLET_INV = Bullet_num("rojo", 1145, 41)
        self.WATERBULLET_INV = Bullet_num("azul", 1195, 41)
        self.WATERBULLET_INV.angle = 90
        self.escudo = Escudo(1300, 41)
        self.money_imagen = Escudo(1300, 770)
        self.gema_roja = Bullet_num("gema_azul", 1300, 708)
        self.gema_azul = Bullet_num("gema_roja", 1300, 658)
        self.Setas = setas(1350, 41)
        self.protagonist.set_up()

        self.physics_engine = arcade.PhysicsEngineSimple(self.protagonist, self.scene["cajas"])
        # self.physics_engine = arcade.PhysicsEngineSimple(self.protagonist,self.scene["colisiones"])

    def on_draw(self):
        self.clear()
        arcade.start_render()

        # Imprimimos el contenido del videojuego.
        self.camera_for_sprites.use()

        self.scene.draw()

        for protagonist in self.protagonist_list:
            protagonist.draw()
        for enemy in self.enemies_list:
            enemy.draw()
        for bullet in self.bullet_list:
            bullet.draw()
        for bullet in self.bullet_enemy_list:
            bullet.draw()
        for mascota in self.mascota_list:
            mascota.draw()

        # Es para ver las
        # for enemy in self.enemies_list:
        #     if enemy.distance() < DISTANCE_TO_ATTACK:
        #         arcade.draw_rectangle_outline(enemy.position[0],
        #                                        enemy.position[1],
        #                                        20,
        #                                        40,
        #                                        arcade.color.RED, 2)
        #         if enemy.line_of_sight():
        #             arcade.draw_line(self.protagonist.position[0],
        #                               self.protagonist.position[1],
        #                               enemy.position[0],
        #                               enemy.position[1],
        #                               arcade.color.RED, 2)
        #
        #     path = enemy.path
        #     if path:
        #         arcade.draw_line_strip(enemy.path, arcade.color.BLUE, 2)
        for enemy in self.enemies_list:
            path = enemy.path
            if path:
                arcade.draw_line_strip(enemy.path, arcade.color.BLUE, 2)

        # Imprimimos la GUI del videojuego
        self.camera_for_gui.use()
        arcade.draw_text(f"Health:{self.protagonist.now_hp()} / {self.protagonist.max_hp()}", 10, 30,
                         arcade.color.WHITE, 24)
        # Imprimimos en la pantalla los numeros de setas y escudos que hay encima del objeto
        arcade.draw_text(f"{self.protagonist.Inventario.get_escudos()}", 1290, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_setas()}", 1340, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_water()}", 1200, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_fire()}", 1150, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_electricity()}", 1100, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_Air()}", 1050, 30, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.Inventario.get_money()}", 1320, 758, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.gemas.get_velocidad()}", 1327, 648, arcade.color.WHITE, 24)
        arcade.draw_text(f"{self.protagonist.gemas.get_tamaño()}", 1327, 698, arcade.color.WHITE, 24)
        self.escudo.draw()
        self.money_imagen.draw()
        self.Setas.draw()
        self.FIREBULLET_INV.draw()
        self.WATERBULLET_INV.draw()
        self.gema_roja.draw()
        self.gema_azul.draw()

    # SACAR ESTO DE COMENTARIO PARA TENER LA CÁMARA MOVIENDO
    # def center_camera_to_player(self):
    #     screen_center_x = self.protagonist.center_x - (self.camera_for_sprites.viewport_width / 2)
    #     screen_center_y = self.protagonist.center_y - (self.camera_for_sprites.viewport_height / 2)
    #
    #     #Don't let camera travel past 0
    #     if screen_center_x < 0:
    #         screen_center_x = 0
    #     if screen_center_y < 0:
    #         screen_center_y = 0
    #
    #     player_centered = screen_center_x, screen_center_y
    #
    #     self.camera_for_sprites.move_to(player_centered)

    def on_update(self, delta_time):
        # SACAR ESTO DE COMENTARIO PARA TENER LA CÁMARA MOVIENDOa
        # self.center_camera_to_player()

        self.timer_mouse += 1

        self.protagonist.Inventario.update(delta_time)
        self.protagonist_list.update()
        for enemy in self.enemies_list:
            enemy.update()
            bullet = enemy.shoot()
            if bullet:
                self.bullet_enemy_list.append(bullet)
        self.bullet_list.update()
        self.bullet_enemy_list.update()
        self.mascota_list.update()

        """ Motor de colisiones """
        for bullet in self.bullet_list:
            # Si la bala sale de los margenes de la pantalla la eliminamos
            if bullet.bottom > SCREEN_HEIGHT or bullet.top < 0 or bullet.right < 0 or bullet.left > SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

            # Tratamiento de la bala en caso de chocar con un obstáculo
            bullet_hit_env_list = arcade.check_for_collision_with_list(bullet, self.scene["cajas"])
            # bullet_hit_env_list = arcade.check_for_collision_with_list(bullet, self.scene["colisiones"])
            if len(bullet_hit_env_list) > 0:
                if bullet.is_moved():
                    bullet.collision()

            # Tratamiento de la bala y del enemigo en caso de chocar entre ellos.
            bullet_hit_enemie_list = arcade.check_for_collision_with_list(bullet, self.enemies_list)
            for enemie in bullet_hit_enemie_list:
                if type(bullet) == src.Bullet_Water.Bullet_Water:
                    if bullet.is_stopped():
                        enemie.gain_life(bullet.get_damage())
                    elif bullet.is_moved():
                        bullet.collision()
                else:
                    if bullet.is_moved() or bullet.is_stopped():
                        enemie.lose_life(bullet.get_damage())
                        bullet.collision()
                if not enemie.alive():
                    enemie.remove_from_sprite_lists()

            # Tratamiento de la bala en caso de chocar con el protagonista
            bullet_hit_protagonist = arcade.check_for_collision_with_list(bullet, self.protagonist_list)
            if len(bullet_hit_protagonist) > 0:
                if type(bullet) == src.Bullet_Water.Bullet_Water:
                    if bullet.is_stopped():
                        self.protagonist.gain_life(bullet.get_damage())

            # Eliminamos aquellas balas que estén muertas, y por tanto ya no tengan utilidad
            if bullet.is_dead():
                bullet.remove_from_sprite_lists()

        "Motor de colisiones para las balas de los enemigos...esto hay que mejorarlo, incluso meterlo con lo anterior"
        for bullet in self.bullet_enemy_list:
            # Si la bala sale de los margenes de la pantalla la eliminamos
            if bullet.bottom > SCREEN_HEIGHT or bullet.top < 0 or bullet.right < 0 or bullet.left > SCREEN_WIDTH:
                bullet.remove_from_sprite_lists()

            # Tratamiento de la bala en caso de chocar con un obstáculo
            bullet_hit_env_list = arcade.check_for_collision_with_list(bullet, self.scene["cajas"])
            # bullet_hit_env_list = arcade.check_for_collision_with_list(bullet, self.scene["colisiones"])
            if len(bullet_hit_env_list) > 0:
                if bullet.is_moved():
                    bullet.collision()

            # Tratamiento de la bala y del enemigo en caso de chocar entre ellos.
            bullet_hit_enemie_list = arcade.check_for_collision_with_list(bullet, self.protagonist_list)
            if len(bullet_hit_enemie_list) > 0:
                if bullet.is_moved() or bullet.is_stopped():
                    self.protagonist.lose_life(bullet.get_damage())
                    bullet.collision()
                if not self.protagonist.alive():
                    self.protagonist.remove_from_sprite_lists()

            # Eliminamos aquellas balas que estén muertas, y por tanto ya no tengan utilidad
            if bullet.is_dead():
                bullet.remove_from_sprite_lists()

        # if len(self.scene["enemies"]) == 0:
        #     game_view = GameOverWindow()
        #     self.window.show_view(game_view)

        # Cuando tengamos nivels con paredes miraremos si la bala choca con la pared y si lo hace desaparece
        # if bullet.bottom > SCREEN_HEIGHT:
        #    bullet.remove_from_sprite_lists()

        # box_hit_list = arcade.check_for_collision_with_list(self.protagonist, self.scene["cajas"])

        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.F3:
            self.F3_pressed = True
            self.mascota_movement()
            self.protagonist.not_move()

        elif key == arcade.key.F4:
            self.F3_pressed = True
            self.mascota.not_move()
            self.protagonist_movement()
            self.mascota.follow_sprite()
        if key == arcade.key.LSHIFT:
            self.protagonist.want_run(True)
        if key == arcade.key.A:
            self.protagonist.want_move_left(True)
        elif key == arcade.key.D:
            self.protagonist.want_move_right(True)
        elif key == arcade.key.W:
            self.protagonist.want_move_up(True)
        elif key == arcade.key.S:
            self.protagonist.want_move_down(True)

        # En el keypress solo debería haber variables de teclas presionadas. Pendiente cambiar esta parte para que la
        # gestión de elementos, setas, etc se haga en otro lado (preferiblemente en la clase protagonist)
        if key == arcade.key.R:
            if self.protagonist.Inventario.get_money() >= 20:
                self.protagonist.Inventario.set_money(self.protagonist.Inventario.get_money() - 20)
                self.protagonist.Inventario.set_fire(self.protagonist.Inventario.get_fire() + 10)
        if key == arcade.key.T:
            if self.protagonist.Inventario.get_money() >= 20:
                self.protagonist.Inventario.set_money(self.protagonist.Inventario.get_money() - 20)
                self.protagonist.Inventario.set_water(self.protagonist.Inventario.get_water() + 10)
        if key == arcade.key.Y:
            if self.protagonist.Inventario.get_money() >= 20:
                self.protagonist.Inventario.set_money(self.protagonist.Inventario.get_money() - 20)
                self.protagonist.Inventario.set_electricity(self.protagonist.Inventario.get_electricity() + 10)
        if key == arcade.key.F:
            if self.protagonist.Inventario.get_money() >= 20:
                self.protagonist.Inventario.set_money(self.protagonist.Inventario.get_money() - 20)
                self.protagonist.Inventario.set_Air(self.protagonist.Inventario.get_Air() + 10)
        elif key == arcade.key.I:
            self.window.show_view(Inventory())
        elif key == arcade.key.Q:
            # Vemos si tenemos escudos en el inventario
            if self.protagonist.Inventario.get_escudos() > 0:
                # Si tiene, realiza su accion y encima se resta uno del inventario
                self.protagonist.gain_life(20)
                self.protagonist.Inventario.set_escudo((self.protagonist.Inventario.get_escudos()) - 1)
        if key == arcade.key.E:
            self.protagonist.Inventario.use_setas()

        # Son solo para probar el tema de la vida (para eliminar)
        # elif key == arcade.key.Q:
        # self.protagonist.lose_life(5)
        # elif key == arcade.key.E:
        # self.protagonist.gain_life(5)

        # Para probar una cosa de las balas, cuando lo acabe lo borro
        elif key == arcade.key.KEY_1:
            self.type_bullet = "air"
        elif key == arcade.key.KEY_2:
            self.type_bullet = "electricity"
        elif key == arcade.key.KEY_3:
            self.type_bullet = "water"
        elif key == arcade.key.KEY_4:
            self.type_bullet = "fire"

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LSHIFT:
            self.protagonist.want_run(False)
        if key == arcade.key.A:
            self.protagonist.want_move_left(False)
        elif key == arcade.key.D:
            self.protagonist.want_move_right(False)
        elif key == arcade.key.W:
            self.protagonist.want_move_up(False)
        elif key == arcade.key.S:
            self.protagonist.want_move_down(False)

    def on_mouse_press(self, x, y, button, modifiers):
        if self.type_bullet == "air":
            if self.protagonist.Inventario.get_Air() > 0:
                self.protagonist.Inventario.set_Air((self.protagonist.Inventario.get_Air()) - 1)
                bullet = self.protagonist.shoot(self.type_bullet, x, y)
                self.bullet_list.append(bullet)
            else:
                print("No hay municion de esta arma")

        if self.type_bullet == "electricity":
            if self.protagonist.Inventario.get_electricity() > 0:
                self.protagonist.Inventario.set_electricity((self.protagonist.Inventario.get_electricity()) - 1)
                bullet = self.protagonist.shoot(self.type_bullet, x, y)
                self.bullet_list.append(bullet)
            else:
                print("No hay municion de esta arma")

        if self.type_bullet == "water":
            if self.protagonist.Inventario.get_water() > 0:
                self.protagonist.Inventario.set_water((self.protagonist.Inventario.get_water()) - 1)
                bullet = self.protagonist.shoot(self.type_bullet, x, y)
                self.bullet_list.append(bullet)
            else:
                print("No hay municion de esta arma")

        if self.type_bullet == "fire":
            self.timer_mouse = 0

    def on_mouse_release(self, x, y, button, modifiers):
        if self.type_bullet == "fire":
            if self.protagonist.Inventario.get_fire() > 0:
                self.protagonist.Inventario.set_fire((self.protagonist.Inventario.get_fire()) - 1)
                bullet = self.protagonist.shoot(self.type_bullet, x, y, self.timer_mouse)
                self.bullet_list.append(bullet)
            else:
                print("No hay municion de esta arma")


class GameOverWindow(arcade.View):

    def __init__(self):

        super().__init__()

        self.enter_pressed = False

        self.option_hovered_on = 1

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        self.clear()
        arcade.start_render()

        if self.option_hovered_on == 1:
            arcade.draw_rectangle_filled(645, 310, 100, 50, arcade.color.GRAY)
        if self.option_hovered_on == 2:
            arcade.draw_rectangle_filled(755, 310, 100, 50, arcade.color.GRAY)
        if self.option_hovered_on == 3:
            arcade.draw_rectangle_filled(700, 210, 200, 50, arcade.color.GRAY)
        arcade.draw_text("GAME OVER", 340, 600, arcade.color.WHITE, 80)
        arcade.draw_text("RETRY?", 590, 500, arcade.color.WHITE, 40)
        arcade.draw_text("YES", 610, 300, arcade.color.WHITE, 24)
        arcade.draw_text("NO", 730, 300, arcade.color.WHITE, 24)
        arcade.draw_text("MAIN MENU", 605, 200, arcade.color.WHITE, 24)

    def on_update(self, delta_time):

        # if self.option_hovered_on > 2:
        #    self.option_hovered_on = 1
        # if self.option_hovered_on < 1:
        #    self.option_hovered_on = 2
        if self.enter_pressed == True:
            if self.option_hovered_on == 1:
                self.window.show_view(MainGame())
            if self.option_hovered_on == 2:
                self.window.close()
            if self.option_hovered_on == 3:
                self.window.show_view(MenuScreen())

    def on_key_press(self, key, modifiers):

        if key == arcade.key.ESCAPE:
            self.window.show_view(MainGame())
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


class PauseMenu(arcade.View):

    def __init__(self):

        super().__init__()

        self.enter_pressed = False

        self.option_hovered_on = 1

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        self.clear()
        arcade.start_render()

        if self.option_hovered_on == 1:
            arcade.draw_rectangle_filled(615, 310, 150, 50, arcade.color.GRAY)
        if self.option_hovered_on == 2:
            arcade.draw_rectangle_filled(777, 310, 70, 50, arcade.color.GRAY)
        if self.option_hovered_on == 3:
            arcade.draw_rectangle_filled(700, 210, 200, 50, arcade.color.GRAY)
        arcade.draw_text("GAME PAUSED", 340, 600, arcade.color.WHITE, 80)
        arcade.draw_text("Continue", 550, 300, arcade.color.WHITE, 24)
        arcade.draw_text("Exit", 750, 300, arcade.color.WHITE, 24)
        arcade.draw_text("MAIN MENU", 605, 200, arcade.color.WHITE, 24)

    def on_update(self, delta_time):

        # if self.option_hovered_on > 2:
        #    self.option_hovered_on = 1
        # if self.option_hovered_on < 1:
        #    self.option_hovered_on = 2
        if self.enter_pressed == True:
            if self.option_hovered_on == 1:
                self.window.show_view(MainGame())
            if self.option_hovered_on == 2:
                self.window.close()
            if self.option_hovered_on == 3:
                self.window.show_view(MenuScreen())

    def on_key_press(self, key, modifiers):

        if key == arcade.key.ESCAPE:
            self.window.show_view(MainGame())
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
