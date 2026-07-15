import random


class Casa:
    def __init__(self, janela: bool, luz: bool) -> None:
        self.temperatura = 23
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

    def ligar_luz(self) -> None:
        aumento_temp = self.temperatura + random.randint(1, 2)
        self.temperatura = aumento_temp

        print('A luz foi ligada!!!')

        print(f'A temperatura atual é: {self.temperatura}')

        tempo_mud = self.minuto + random.randint(1, 3)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

    def abrir_janela(self) -> None:
        aumento_temp = self.temperatura + random.randint(2, 1)
        self.temperatura = aumento_temp

        print('A janela foi aberta!!!')

        print(f'A temperatura atual é: {self.temperatura}')

        tempo_mud = self.minuto + random.randint(1, 4)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')
