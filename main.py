import random
import os
import subprocess


def limpar_tela() -> None:
    comando = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(comando, shell=True)


def pausar() -> None:
    input('\nPressione Enter para continuar...')


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
        if self.luz:
            print('A luz ja esta ligada!!!')
            return

        self.temperatura += random.randint(1, 2)

        print('A luz foi ligada!!!')

        print(f'A temperatura atual é: {self.temperatura} ºC')

        tempo_mud = random.randint(1, 3)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

        self.luz = True

    def abrir_janela(self) -> None:
        if self.janela:
            print('A janela ja esta aberta')
            return

        self.temperatura += random.randint(2, 3)

        print('A janela foi aberta!!!')

        print(f'A temperatura atual é: {self.temperatura} ºC')

        tempo_mud = random.randint(2, 4)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

        self.janela = True

    def desligar_luz(self) -> None:
        if not self.luz:
            print('A luz ja esta desligada!!!')
            return

        self.temperatura -= random.randint(1, 2)

        print('A luz foi desligada!!!')

        print(f'A temperatura atual é: {self.temperatura} ºC')

        tempo_mud = random.randint(1, 3)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

        self.luz = False

    def fechar_janela(self) -> None:
        if not self.janela:
            print('A janela ja esta fechadaa!!!')
            return

        self.temperatura -= random.randint(2, 3)

        print('A janela foi fechada!!!')

        print(f'A temperatura atual é: {self.temperatura} ºC')

        tempo_mud = random.randint(2, 4)

        self._avançar_tempo(tempo_mud)

        print(f'Hora atual: {self.hora:02}:{self.minuto:02}')

        self.janela = False

    def mostrar_status(self) -> None:
        if self.luz:
            print('A luz está ligada!!!')

        else:
            print('A Luz está desligada!!!')

        if self.janela:
            print('A janela está aberta!!!')

        else:
            print('A janela esta fechada!!!')


def main() -> None:
    casa = Casa(False, False)

    while True:
        print('\n')
        print('---------- Casa automatizada ---------- \n')
        print('1 - Ligar Luz')
        print('2 - Abrir a Janela')
        print('3 - Desligar Luz')
        print('4 - Fechar a Janela')
        print('5 - Mostrar Status')
        print('6 - Sair do Sistema\n')
        print('-------------------------------------\n')

        deseja_fazer: str = input('O que você deseja fazer (1, 2, 3, 4, 5 ou 6)? ')
        print('\n')

        match deseja_fazer:
            case '1':
                casa.ligar_luz()

            case '2':
                casa.abrir_janela()

            case '3':
                casa.desligar_luz()

            case '4':
                casa.fechar_janela()

            case '5':
                casa.mostrar_status()

            case '6':
                print('Obrigado por usar o sistema!!!')
                break

            case _:
                print('Opção inválida!!!')

        if deseja_fazer != '6':
            pausar()
            limpar_tela()


if __name__ == '__main__':
    main()
