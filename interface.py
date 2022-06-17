#mes bateaux en bleu
#mes bateaux touchÃ©s en rouge 
#mes mines non touchÃ©s en vert
#mes mines touchÃ©s en orange 

from tkinter import *
import tkinter as tk 
from tkinter import ttk
import numpy as np


def scores ():
    score_window = tk.Tk()
    score_window.title("scoreboard")
    #score_window.attributes("-fullscreen", True)
    score_window.geometry("+0+0")
    score_window.geometry("1000x980")
    score_window.config(background='#7dbbf5')
    button3 = tk.Button(score_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[score_window.destroy(),main()])
    button3.pack()

def play ():
    game_window = tk.Tk()
    game_window.title("game")
    #game_window.attributes("-fullscreen", True)
    game_window.geometry("+0+0")
    game_window.geometry("1000x980")
    game_window.config(background='#7dbbf5')
    
    largeurCanvas, hauteurCanvas = 800, 800
    nbUnite = 10
    tailleUnite = largeurCanvas / nbUnite
    
    def calculeMax():
        
        return int(largeurCanvas/(tailleUnite * 2)), int(hauteurCanvas/(tailleUnite *
                                                                        2))
    def coo(x,y):
        
        return largeurCanvas/2+x*tailleUnite, hauteurCanvas/2-y*tailleUnite
    
    def initGraphique():
        
        for l in range(-maxy+1, maxy):
            feuille.create_line(coo(-maxx,l),coo(maxx,l), width=1, fill='black', dash=(5,3))
            feuille.create_line(coo(-maxx,0),coo(maxx,0), width=2, fill='black')
            
        for c in range(-maxx+1, maxx):
            feuille.create_line(coo(c,-maxy),coo(c,maxy), width=1, fill='black', dash=(5,3))
            feuille.create_line(coo(0,-maxy),coo(0,maxy), width=2, fill='black')
  
    maxx, maxy = calculeMax()
    feuille = Canvas(game_window, width=largeurCanvas, height=hauteurCanvas, bg='grey')
    feuille.pack()
    initGraphique()
    boutonAdd = Button(game_window, text="ajouter", command=lambda: add())
    boutonAdd.place(x = 900, y = 900)
    
    input_X = Text(game_window,height = 1,width = 5)
    input_X.place(x = 100, y = 900)
    
    input_Y = Text(game_window,height = 1,width = 5)
    input_Y.place(x = 300, y = 900)
    
    button3 = tk.Button(game_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[game_window.destroy(),main()])
    button3.pack()
    

def parameters ():
    
    param_window = tk.Tk()
    param_window.title("param")
    #param_window.attributes("-fullscreen", True)
    param_window.geometry("+0+0")
    param_window.geometry("1000x980")
    param_window.config(background='#6b6e6c')
    set_difficulty = ttk.Combobox(param_window)
    set_difficulty['values'] = ('easy', 'medium', 'hard')
    set_difficulty['state'] = 'readonly'
    val = set_difficulty.get()
    set_difficulty.pack()
    button3 = tk.Button(param_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[param_window.destroy(),main()])
    button3.pack()
    

def main ():
    main_window = tk.Tk()
    main_window.title("Battleship")
    #main_window.attributes("-fullscreen", True)
    main_window.geometry("+0+0")
    main_window.geometry("1000x980")
    main_window.config(background='#7dbbf5')
    button1 = tk.Button(main_window, text="Jouer", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[main_window.destroy(),play()])
    button2 = tk.Button(main_window, text="Score", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[main_window.destroy(),scores()])
    button3 = tk.Button(main_window, text="parametres", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[main_window.destroy(),parameters()])
    button4 = tk.Button(main_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=main_window.destroy)
    title = tk.Label(main_window, text="Battleship Game", font=("Courrier", 40), bg='#7dbbf5', fg='black')
    
    
    title.pack(expand = True)
    button1.pack(expand=True)
    button2.pack(expand=True)
    button3.pack(expand=True)
    button4.pack()
    main_window.mainloop() 
    
main()
