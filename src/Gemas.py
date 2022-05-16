import arcade


class Gemas():

    def __init__(self, n_velocidad,n_tamaño ):
        self.n_velocidad=n_velocidad
        self.n_tamaño=n_tamaño

    def get_velocidad(self):
        return self.n_velocidad
    def get_tamaño(self):
        return self.n_tamaño
    def set_tamaño(self,tamaño):
        self.n_tamaño=tamaño
    def set_velocidad(self,velocidad):
        self.velocidad=velocidad