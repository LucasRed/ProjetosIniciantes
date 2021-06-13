from random import randint
import PySimpleGUI as sg


class ChuteNumero:
    def __init__(self):
        self.valor_random = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def gerar_numero(self):
        self.valor_random = randint(self.valor_minimo, self.valor_maximo)

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('                             Seu chute')],
            [sg.Input(size=(33, 0), key='Chute'), sg.Button('Chutar!')],
            [sg.Output(size=(39, 0))]
        ]
        # criar a janela
        self.janela = sg.Window('Acerte o número!', layout=layout)
        self.gerar_numero()
        try:
            while True:
                # receber os valores
                self.events, self.values = self.janela.read()
                # Utilizar os valores
                if self.events == sg.WIN_CLOSED:
                    break
                if self.events == 'Chutar!':
                    self.chute = self.values['Chute']
                    while self.tentar_novamente:
                        if int(self.chute) < self.valor_random:
                            print('Tente um valor mais alto!\n')
                            break
                        elif int(self.chute) > self.valor_random:
                            print('Tente um valor mais baixo!\n')
                            break
                        elif int(self.chute) == self.valor_random:
                            print('VOCÊ ACERTOU!')
                            self.tentar_novamente = False
                            break
        except:
            print('Houve um erro ao receber seu valores')


acerto = ChuteNumero()
acerto.iniciar()
