from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
import time
import json

# cores ---------------
co0 = "#444466"  # Preta / black
co1 = "#feffff"  # branca / white 
co2 = "#6f9fbd"  # azul / blue
fundo = "#484f60"

#Parametros Janela ---------------
nomeJanela = "Bitcoin Price Tracker"
tamanhoJanela = "320x350"

# Criando janela ---------------
janela = Tk()
janela.title(nomeJanela)
janela.geometry(tamanhoJanela)
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# Dividindo a janela em dois frames ---------------
framePrincipal = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief='flat')
framePrincipal.grid(row=1, column=0)

frameCorpo = Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief='flat')
frameCorpo.grid(row=2, column=0, sticky=NW)

# função para retornar cotação
def info():
    apiLink = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CBRL'

    # HTTP Requests ---------------
    response = requests.get(apiLink)

    # Convertendo os dados em dict ---------------
    dados = response.json()

    # Passando os valores para variaveis ---------------
    valorUSD = float(dados['USD'])
    valorEuro = float(dados['EUR'])
    valorReal = float(dados['BRL'])

    # Formatando os valores ---------------
    valorUSD = "${:,.3f}".format(valorUSD)
    valorEuro = "€{:,.3f}".format(valorEuro)
    valorReal = "R${:,.3f}".format(valorReal)
    
    # Entregando os valores ao corpo ---------------
    lPUSD['text'] = valorUSD
    lPEuro['text'] = valorEuro
    lPReal['text'] = valorReal
    
    frameCorpo.after(500, info)


# Configurando o frame principal ---------------
imagem = Image.open(r'.\Imagens\bitcoin.png')
imagem = imagem.resize((30,30), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

lIcon = Label(framePrincipal, image=imagem, compound=LEFT, bg=co1, relief=FLAT)
lIcon.place(x=10, y=10)

lNome = Label(framePrincipal, text='Bitcoin Price Tracker', bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Arial 20'))
lNome.place(x=50, y=5)

# Configurando o frame corpo ---------------

lPUSD = Label(frameCorpo, text='', width=14, bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 20'))
lPUSD.place(x=0, y=50)

lPEuro = Label(frameCorpo, text='', width=14, bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 20'))
lPEuro.place(x=0, y=80)

lPReal = Label(frameCorpo, text='', width=14, bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 20'))
lPReal.place(x=0, y=110)

info()

janela.mainloop()
