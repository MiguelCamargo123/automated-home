import random


class casa:
    def __init__(self, temperatura: int, janela: bool, luz: bool) -> None:
        self.temperatura = temperatura
        self.janela = janela
        self.luz = luz
        self.hora = 6
        self.minuto = 0
