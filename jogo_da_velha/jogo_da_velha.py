from tkinter import *
from tkinter import ttk


jogador = True
contador = 0
jogada = 0
jogadas = [1,2,3,4,5,6,7,8,9]
continuar = True
jogar = True
botoes = []

def recolocar_frame(frame, relx, rely, relwidth, relheight):
    frame.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)

def fechar_jogo():
    global janela
    janela.destroy()


def esperar(funcao):
    janela.after(3000, funcao)


def frame_overlay():
    global jogar, var2
    def clicar_jogar():
        global jogar, var2
        jogar = not jogar
        print("Clicou no botão!")
        var2.set(1)

    #configurando a janela de pergunta:
    overlay = Frame(janela, bg=azul_lobby)
    overlay.place(relx=0.25, rely = 0.2, relheight= 0.4, relwidth=0.5)
    overlay.lift()

    
    #ocultar o frame indicador
    frame_indicador.place_forget()


    #label da logo do jogo da velha
    label_logo = Label(overlay, text="J O G O   D A   V E L H A", fg=dourado, bg=azul_lobby, font=("my game", 13))
    label_logo.place(relx=0, rely=0.1 , relwidth=1, relheight=0.2)
    
    #o botão para clicar com a intenção de jogar
    botao_jogar = Button(overlay, text="I N I C I A R   J O G O", command= clicar_jogar, bg=branco, borderwidth=0, font=("my game", 9), fg=verde)
    botao_jogar.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.2)
    

    #configurando o botão de não querer jogar:
    botao_fechar = Button(overlay, text="F E C H A R    J O G O", command= fechar_jogo, bg=branco, borderwidth=0, font=("my game", 9), fg=vermelho)
    botao_fechar.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.2)

    desabilitar_frame(frame_grade)
    overlay.wait_variable(var2)
    overlay.destroy()
    habilitar_frame(frame_grade)


def mudar_jogador():
    if continuar==False:
        if jogador and contador!=8:
            label_indicador.config(text="Parabéns ao jogador 1, o vencedor!", fg=dourado)
        elif contador==8:
            label_indicador.config(text="Empatou, joguem novamente!", fg=roxo)
        else:
            print("erro")
            label_indicador.config(text="Parabéns ao jogador 2, o vencedor!", fg=dourado)
    elif jogador:
        label_indicador.config(text="Vez do Jogador 1")
    else:
        label_indicador.config(text="Vez do jogador 2")


def desabilitar_frame(frame):
    for child in frame.winfo_children():
        try:
            child.configure(state='disabled')
        except TclError:
            pass


def habilitar_frame(frame):
    for child in frame.winfo_children():
        try:
            child.configure(state='normal')
        except TclError:
            pass

def cliclar_botao(buttonid, botao):
    global jogada
    global contador
    #posição da jogada do usuário:
    if buttonid in jogadas:
        jogadas.remove(buttonid)
        jogada = buttonid
        var.set(buttonid)
        print(jogador)
        print(continuar)
        print(contador)

        #botar o simbolo aonde a pessoa jogou:
        if jogador==True and continuar:
            botao.config(text="❌", font=("Verdana", 35), fg="#FF00FF")
        elif not jogador and continuar:
            botao.config(text="⭕", font=("Verdana", 35), fg="#00FFFF")


#tem que criar uma função que vai resetar todas as configurações para o jogo ocorrer novamente:

def  resetar_jogo():
    global jogador, jogar, var, var2, jogada, jogadas, continuar, contador, botoes
     

    #zerar as variáveis:
    jogador = True
    contador = 0
    jogada = 0
    jogadas = [1,2,3,4,5,6,7,8,9]
    continuar = True
    jogar = True
    var.set(0)
    var2.set(0)


    #zerar a grade de jogo:
    for btn in botoes:
        btn.config(text="")

    main_loop()

#cores
roxo = "#4f0180"
roxo_neon = "#ad6ed4"
azul = '#73cbeb'
azul_lobby = "#302d5c"
azul_escuro =  "#00008B"
dourado = "#B8860B"
branco = "#FFFFFF"
verde = "#238E23"
vermelho = "#8b0000"

#configurações principais
janela = Tk()
janela.geometry('500x650')
janela.title('Joogo da velha')
janela.config(bg=roxo)
var2 = IntVar(value=0)
var = IntVar(value=0)



#frame das linhas do jogo de xadrez
frame_grade = Frame(janela, bg=roxo)
frame_grade.place(relx=0.17, rely=0.15, relwidth=0.66, relheight=0.5)


#frame do indicador de jogador
frame_indicador = Frame(janela, bg=branco, borderwidth=2, relief="groove")
frame_indicador.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.1)
label_indicador = Label(frame_indicador, text = "Vez do jogador 1", fg=azul_escuro, bg=branco, font=("Verdana", 14, "bold"))
label_indicador.pack(expand=True, fill="both")


#frame para o loby
#frame_lobby = Frame(janela, bg=azul_lobby)
#frame_lobby.place(relx=0.19, rely=0.1, relwidth=0.62, relheight=0.8)

#linhas do jogo da velha:
linha1_h = Frame(frame_grade, bg= roxo_neon)
linha1_h.place(relx=0, rely=0.3, relwidth=1, relheight=0.018)

linha2_h = Frame(frame_grade, bg= roxo_neon)
linha2_h.place(relx=0, rely=0.6, relwidth=1, relheight=0.018)

linha1_v = Frame(frame_grade, bg= roxo_neon)
linha1_v.place(relx=0.33, rely=0, relwidth=0.018, relheight=1)

linha2_v = Frame(frame_grade, bg= roxo_neon)
linha2_v.place(relx=0.66, rely=0, relwidth=0.018, relheight=1)

#botões para o jogo:
botao1 = Button(frame_grade,  command= lambda: cliclar_botao(int(1), botao1), bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao1.place(relx=0, rely=0, relwidth=0.33, relheight=0.3)
botoes.append(botao1)

botao2 = Button(frame_grade, command= lambda: cliclar_botao(int(2), botao2), bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao2.place(relx=0.35, rely=0, relwidth=0.31, relheight=0.3)
botoes.append(botao2)

botao3 = Button(frame_grade, command= lambda: cliclar_botao(int(3), botao3), bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao3.place(relx=0.68, rely=0, relwidth=0.33, relheight=0.3)
botoes.append(botao3)

botao4 = Button(frame_grade, command= lambda: cliclar_botao(int(4), botao4), bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao4.place(relx=0., rely=0.32, relwidth=0.33, relheight=0.28)
botoes.append(botao4)

botao5 = Button(frame_grade, command= lambda: cliclar_botao(int(5), botao5), bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao5.place(relx=0.35, rely=0.32, relwidth=0.31, relheight=0.28)
botoes.append(botao5)

botao6 = Button(frame_grade, command= lambda: cliclar_botao(int(6), botao6),  bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao6.place(relx=0.68, rely=0.32, relwidth=0.33, relheight=0.28)
botoes.append(botao6)

botao7 = Button(frame_grade, command= lambda: cliclar_botao(int(7), botao7), bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao7.place(relx=0., rely=0.62, relwidth=0.33, relheight=0.38)
botoes.append(botao7)

botao8 = Button(frame_grade, command= lambda: cliclar_botao(int(8), botao8), bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao8.place(relx=0.35, rely=0.62, relwidth=0.31, relheight=0.38)
botoes.append(botao8)

botao9 = Button(frame_grade, command= lambda: cliclar_botao(int(9), botao9), bg=roxo, borderwidth=0, highlightthickness=0, relief="flat")
botao9.place(relx=0.68, rely=0.62, relwidth=0.33, relheight=0.38)
botoes.append(botao9)
#desabilitar_frame(frame_grade)



def main_loop():
    global contador
    global jogadas
    global jogada
    global continuar 
    global jogador
    mapear_grade = []

    #chamar a janela principal:
    frame_overlay()

    #ativar o frame indicador:
    recolocar_frame(frame_indicador, relx=0.1, rely=0.75, relwidth=0.8, relheight=0.1)

    #montar a grade para a analise:
    for _ in range (1,4):
        linha = []
        for _ in range (1,4):
            contador += 1
            linha.append(f"{contador}")
        mapear_grade.append(linha)
    contador = 0

    label_indicador.config(text="Vez do Jogador 1")
    #algoritmo do jogo da velha:
    while continuar:
        #comando para esperar o usuário apertar algum botão:
        frame_grade.wait_variable(var)

        #modificar a jogada na grade(mapear_grade) que vai ser analisada:
        if jogador:
            for l in range (0,3):
                for c in range(0,3):
                    if mapear_grade[l][c]==str(jogada):
                        mapear_grade[l][c]='X'
        else:
            for l in range (0,3):
                for c in range(0,3):
                    if mapear_grade[l][c]==str(jogada):
                        mapear_grade[l][c]='O'


        #verificar se alguém já ganhou:
        for i in range (0,3):
            if mapear_grade[i][0]==mapear_grade[i][1] and mapear_grade[i][0]==mapear_grade[i][2]:
                if  jogador:
                    print('Parabéns ao jogador 1, o vencedor!!')
                else:
                    print('Parabéns ao jogador 2, o vencedor!!')
                continuar = False
                break
        for k in range (0,3):
            if mapear_grade[0][k]==mapear_grade[1][k] and mapear_grade[0][k]==mapear_grade[2][k]:
                if  jogador:
                    print('Parabéns ao jogador 1, o vencedor!!')
                else:
                    print('Parabéns ao jogador 2, o vencedor!!')
                continuar = False
                break
        if continuar==False:
            break
        elif mapear_grade[0][0] == mapear_grade[1][1] == mapear_grade[2][2]:
            if  jogador:
                print('Parabéns ao jogador 1, o vencedor!!')
            else:
                print('Parabéns ao jogador 2, o vencedor!!')
            continuar = False
            break
        elif mapear_grade[0][2] == mapear_grade [2][0] == mapear_grade[1][1]:
            if  jogador:
                print('Parabéns ao jogador 1, o vencedor!!')
                print("aqui")
            else:
                print('Parabéns ao jogador 2, o vencedor!!')
            continuar = False
            break
        elif contador==8:
            continuar = False
            break
        contador += 1
        jogador = not jogador
        mudar_jogador()
    mudar_jogador()
    esperar(resetar_jogo)

janela.after(100, main_loop)
janela.mainloop()
