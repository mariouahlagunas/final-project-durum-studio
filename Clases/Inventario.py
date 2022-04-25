import arcade


class inventario(arcade.Sprite):
    def __init__(self, num_escudos, num_setas):
        self.num_escudos = num_escudos
        self.num_setas = num_setas

    def get_escudos(self):
        return self.num_escudos

    def get_setas(self):
        return self.num_setas

    def set_escudo(self, n_escudo):
        self.num_escudos = n_escudo

    def set_setas(self, n_setas):
        self.num_setas = n_setas
