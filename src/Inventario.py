import arcade


class inventario(arcade.Sprite):
    def __init__(self, num_escudos, num_setas, num_fire, num_water):
        self.num_fire = num_fire
        self.num_water = num_water
        self.num_escudos = num_escudos
        self.num_setas = num_setas

    def get_escudos(self):
        return self.num_escudos
    def get_fire(self):
        return self.num_fire
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