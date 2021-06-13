from random import randint
import PySimpleGUI as sg
from time import sleep


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('                                  Jogar dado?')],
            [sg.Button('Sim', size=(20, 0)), sg.Button('Não', size=(20, 0))],
            [sg.Output(size=(48, 0))]
        ]

    def gerar_dado(self):
        print(randint(self.valor_minimo, self.valor_maximo), '\n')

    def iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de dado', layout=self.layout)
        while True:
            # Ler os valores da tela
            self.eventos, self.valores = self.janela.read()
            # Usar valores
            try:
                if self.eventos == 'Sim':
                    self.gerar_dado()
                elif self.eventos == 'Não' or self.eventos == sg.WIN_CLOSED:
                    print('Obrigado, por utilizar nosso sistema!\nAté mais')
                    sleep(2)
                    break
            except:
                print('Ocorreu um erro ao receber sua resposta')


dado = SimuladorDeDado()
dado.iniciar()
