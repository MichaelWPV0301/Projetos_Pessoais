from tkinter import *
from tkinter import ttk


#cores:
preto = "#000000"
azul = "#38576b"
branco = "snow"
amarelo = 'dark orange'
cinza = 'gainsboro'
vermelho = 'brown1'

class Calculadora():
    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Calculadora')
        self.janela.geometry("472x635")
        self.janela.config(bg = preto)
        self.frame_tela = Frame(self.janela, bg=azul)
        self.frame_tela.place(relwidth=1, relheight=0.15, relx=0, rely=0)
        self.frame_corpo = Frame(self.janela, bg=branco)
        self.frame_corpo.place(relwidth=1, relheight=0.85, relx=0, rely=0.15)
        self.resultado = ''
        self.calculo = ''
        self.valores = ''
        self.valor_resultado = StringVar()
        self.valor_digitados = StringVar()
        self.app_label = Label(self.frame_tela, textvariable= self.valor_digitados, font=("Verdana", 18), relief=GROOVE, anchor="e",padx=7)
        self.app_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.historico = Label(self.frame_tela, textvariable= self.valor_resultado, font=("Verdana", 10), anchor="ne",padx=7)
        self.historico.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        self.botoes = {}

    def cria_botão(self,text, linha, posicao, cor=cinza):
        self.botoes[text] = Button(self.frame_corpo, command=lambda: self.calcular(text), text=text, font=("Verdana", 18))
        self.botoes[text].configure(bg=cor)
        self.botoes[text].place(relx=posicao, rely=linha, relwidth=0.25, relheight=0.2)

    def run(self):
            #linha 1:
            self.cria_botão('C', 0, 0, vermelho)
            self.cria_botão('xʸ', 0, 0.25, cinza)
            self.cria_botão('%', 0, 0.5, cinza)
            self.cria_botão("/", 0, 0.75, amarelo)

            #linha 2:
            self.cria_botão('7', 0.2, 0, cinza)
            self.cria_botão('8', 0.2, 0.25, cinza)
            self.cria_botão('9', 0.2, 0.5, cinza)
            self.cria_botão("*", 0.2, 0.75, amarelo)
            
            #linha 3:
            self.cria_botão('4', 0.4, 0, cinza)
            self.cria_botão('5', 0.4, 0.25, cinza)
            self.cria_botão('6', 0.4, 0.5, cinza)
            self.cria_botão("-", 0.4, 0.75, amarelo)

            #linha 4:
            self.cria_botão('1', 0.6, 0, cinza)
            self.cria_botão('2', 0.6, 0.25, cinza)
            self.cria_botão('3', 0.6, 0.5, cinza)
            self.cria_botão("+", 0.6, 0.75, amarelo)

            #linha 5:
            self.cria_botão('\u232B', 0.8, 0, vermelho)
            self.cria_botão('0', 0.8, 0.25, cinza)
            self.cria_botão(',', 0.8, 0.5, cinza)
            self.cria_botão("=", 0.8, 0.75, amarelo)
            self.janela.mainloop()
    
    def calcular(self, evento):
        operadores = "Cxʸ%/*-+\u232B=,"
        if evento not in operadores:
            self.valores += evento
            self.calculo += evento
            self.resultado += evento
            self.valor_digitados.set(self.valores)
            self.valor_resultado.set(self.resultado)
        elif evento in operadores and evento not in '=C\u232B,':
            #any(x in operadores for x in self.calculo)
            #self.valor_resultado += evento
            self.valor_resultado.set(self.resultado.replace('.',','))
            if any(x in self.calculo for x in operadores) and evento!='xʸ':
                if self.calculo[-1] in operadores:
                    pass
                else:
                    self.resultado += str(evento)
                    self.valor_resultado.set(self.resultado.replace('.',','))
                    self.valores = ''
                    self.calculo = str(eval(self.calculo))
                    self.valor_digitados.set(self.calculo.replace('.',','))
                    self.calculo += evento
            elif evento=='xʸ':
                if "**" in self.valores[-1] or self.valores=='':
                    pass
                elif "**" in self.calculo:
                    self.resultado += "^"
                    self.valor_resultado.set(self.resultado.replace('.',','))
                    self.valores = ''
                    self.calculo = str(eval(self.calculo))
                    self.valor_digitados.set(self.calculo.replace('.',','))
                    self.calculo += "**"
                else:
                    self.resultado +="^"
                    self.valor_resultado.set(self.resultado.replace('.',','))
                    self.calculo += "**"
                    self.valores = ''
                    self.valor_digitados.set(self.valores)
            else:
                self.resultado += str(evento)
                self.valor_resultado.set(self.resultado.replace('.',','))
                self.calculo += evento
                self.valores = ''
                self.valor_digitados.set(self.valores)
        elif evento in "C\u232B,":
            if evento == "C":
                self.resultado = ''
                self.calculo = ''
                self.valores = ''
                self.valor_digitados.set(self.valores)
                self.valor_resultado.set(self.resultado)
            elif evento=='\u232B':
                self.resultado = self.resultado[:-1]
                self.valores = self.valores[:-1]
                self.calculo = self.calculo[:-1]
                self.valor_digitados.set(self.valores)
                self.valor_resultado.set(self.resultado)
            else:
                if ',' in self.valores or self.valores=='':
                    pass
                else:
                    self.resultado += ','
                    self.valores += ','
                    self.calculo += '.'
                self.valor_digitados.set(self.valores)
                self.valor_resultado.set(self.resultado)
        elif evento=='=':
            self.resultado += evento
            self.valores =  ''
            self.calculo = str(eval(self.calculo))
            self.valor_resultado.set(self.resultado)
            self.resultado = self.calculo
            self.valor_digitados.set(self.calculo.replace('.',','))