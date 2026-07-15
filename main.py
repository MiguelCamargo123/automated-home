import random


class Casa:
    def __init__(self, temperatura: int, janela: bool, luz: bool) -> None:
        self.temperatura = temperatura
        self.janela = janela
        self.luz = luz
        self.hora = 6
        self.minuto = 0

    def _avançar_tempo(self, minutos: int) -> None:
        self.minuto += minutos

        while self.minuto >= 60:
            self.minuto -= 60
            self.hora += 1

        if self.hora >= 24:
            self.hora = 0
