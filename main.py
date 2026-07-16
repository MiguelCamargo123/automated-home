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
        self.temperatura += random.randint(1, 2)

        print('A luz foi ligada!!!')

        print(f'A temperatura atual é: {self.temperatura} ºC')

        tempo_mud = random.randint(1, 3)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

        self.janela = True

    def abrir_janela(self) -> None:
        self.temperatura += random.randint(2, 3)

        print('A janela foi aberta!!!')

        print(f'A temperatura atual é: {self.temperatura} ºC')

        tempo_mud = random.randint(2, 4)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

        self.janela = True

    def desligar_luz(self) -> None:
        self.temperatura -= random.randint(1, 2)

        print('A luz foi desligada!!!')

        print(f'A temperatura atual é: {self.temperatura} ºC')

        tempo_mud = random.randint(1, 3)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

        self.luz = False

    def fechar_janela(self) -> None:
        self.temperatura -= random.randint(2, 3)

        print('A janela foi fechada!!!')

        print(f'A temperatura atual é: {self.temperatura} ºC')

        tempo_mud = random.randint(2, 4)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

        self.janela = False


def main() -> None:
    casa = Casa(False, False)

    while True:
        print('---------- Casa automatizada ---------- ')
        print()
        print('1 - Ligar Luz')
        print('2 - Abrir a Janela')
        print('3 - Desligar Luz')
        print('4 - Fechar a Janela')
        print('5 - Mostrar Status')
