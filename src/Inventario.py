import arcade


class inventario(arcade.Sprite):
    def __init__(self, num_escudos, num_setas, num_fire, num_water, num_electricity, num_Air, money):
        self.money=money
        self.num_electricity= num_electricity
        self.num_Air=num_Air
        self.num_fire = num_fire
        self.num_water = num_water
        self.num_escudos = num_escudos
        self.num_setas = num_setas
        self.timer_setas = 0
        self.speed_potion_activated = False

    def get_escudos(self):
        return self.num_escudos
    def get_money(self):
        return self.money
    def set_money(self,num_money):
        self.money=num_money
    def get_fire(self):
        return self.num_fire
    def get_Air(self):
        return self.num_Air
    def get_electricity(self):
        return self.num_electricity
    def set_electricity(self, n_electricity):
        self.num_electricity = n_electricity
    def set_Air(self, n_Air):
        self.num_Air = n_Air
    def set_fire(self, n_fire):
        self.num_fire = n_fire
    def get_water(self):
        return self.num_water
    def set_water(self, n_water):
        self.num_water = n_water
    def get_setas(self):
        return self.num_setas
    def set_escudo(self, n_escudo):
        self.num_escudos = n_escudo
    def set_setas(self, n_setas):
        self.num_setas = n_setas

    def use_setas(self):
        if not self.speed_potion_activated and self.num_setas > 0:
            self.speed_potion_activated = True
            self.num_setas -= 1
            self.timer_setas = 5

    def update(self, delta_time):
        if self.timer_setas > 0:
            self.timer_setas -= delta_time
            print(self.timer_setas)
        elif self.speed_potion_activated:
            self.speed_potion_activated = False


