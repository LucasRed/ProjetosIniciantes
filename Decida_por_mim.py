from random import choice
import PySimpleGUI as sg


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso, Não!',
            'Acho que tá na hora certa!'
        ]

    def iniciar(self):
        layout = [
            [sg.Text('Sua pergunta:'), sg.Input()],
            [sg.Button('Decida por mim!')],
            [sg.Output()]
        ]
        # Criar janela
        self.janela = sg.Window('Decida por mim', layout=layout)
        while True:
            # Pegar os dados
            self.events, self.values = self.janela.read()
            # Usar os dados
            if self.events == 'Decida por mim!':
                print(choice(self.respostas))
            if self.events == sg.WIN_CLOSED:
                break


decida = DecidaPorMim()
decida.iniciar()
