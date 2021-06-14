import PySimpleGUI as sg


class JogoAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte eu ou sul?'
        self.pergunta2 = 'Você prefere a espada ou escudo?'
        self.pergunta3 = 'Qual é a sua especialidade?'
        self.finalHistoria1 = 'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'

    def ler_dados(self):
        self.window, self.event, self.values = sg.read_all_windows()

    def fechar(self):
        if self.event == sg.WIN_CLOSED:
            return True

    def again(self):
        self.janela4.hide()
        self.iniciar()

    def iniciar(self):
        # Telas
        tela1 = [
            [sg.Text(self.pergunta1)],
            [sg.Button('Norte', size=(10, 0)), sg.Button('Sul', size=(10, 0))]
        ]
        self.janela1 = sg.Window('Pergunta1', layout=tela1, finalize=True)

        tela2 = [
            [sg.Text(self.pergunta2)],
            [sg.Button('Espada', size=(11, 0)), sg.Button('Escudo', size=(11, 0))]
        ]
        self.janela2 = None

        tela3 = [
            [sg.Text(self.pergunta3)],
            [sg.Button('Linha de frente', size=(20, 0))],
            [sg.Button('Tatico', size=(20, 0))]
        ]
        self.janela3 = None

        tela4 = [
            [sg.Output(size=(50, 0))],
            [sg.Button('Tente de novo'), sg.Button('Sair')]
        ]
        self.janela4 = None

        while True:
            # Ler os dados
            self.ler_dados()
            # Usar os dados
            if self.fechar():
                break
            if self.window == self.janela1:
                if self.event == 'Norte':

                    self.janela1.hide()
                    self.janela2 = sg.Window('Pergunta2', layout=tela2, finalize=True)
                    self.ler_dados()

                    if self.event == 'Espada':
                        self.janela2.hide()
                        self.janela4 = sg.Window('Resposta', layout=tela4, finalize=True)
                        print(self.finalHistoria1)
                        self.ler_dados()
                        if self.event == 'Tente de novo':
                            self.again()
                        if self.fechar() or self.event == 'Sair':
                            break
                    elif self.event == 'Escudo':
                        self.janela2.hide()
                        self.janela4 = sg.Window('Resposta', layout=tela4, finalize=True)
                        print(self.finalHistoria2)
                        self.ler_dados()
                        if self.event == 'Tente de novo':
                            self.again()
                        if self.fechar() or self.event == 'Sair':
                            break

                elif self.event == 'Sul':

                    self.janela1.hide()
                    self.janela3 = sg.Window('Pergunta3', layout=tela3, finalize=True)
                    self.ler_dados()

                    if self.event == 'Linha de frente':
                        self.janela3.hide()
                        self.janela4 = sg.Window('Resposta', layout=tela4, finalize=True)
                        print(self.finalHistoria3)
                        self.ler_dados()
                        if self.event == 'Tente de novo':
                            self.again()
                        if self.fechar() or self.event == 'Sair':
                            break
                    elif self.event == 'Tatico':
                        self.janela3.hide()
                        self.janela4 = sg.Window('Resposta', layout=tela4, finalize=True)
                        print(self.finalHistoria4)
                        self.ler_dados()
                        if self.event == 'Tente de novo':
                            self.again()
                        if self.fechar() or self.event == 'Sair':
                            break


jogo = JogoAventura()
jogo.iniciar()
