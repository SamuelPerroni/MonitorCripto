from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps, ImageDraw
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

# Configurando o frame cima ---------------
style = ttk.Style(framePrincipal)
style.theme_use("clam")

janela.mainloop()