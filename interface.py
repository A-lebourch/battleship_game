from tkinter import *
import tkinter as tk 
from tkinter import ttk
import numpy as np
from bateaux_CLASSE import * 

def available (row, collums):
    available = []
    for a1 in range(1,collums+1):
        for a2 in range(1,row+1):
            position_xy = [a2, a1]
            available.append(position_xy)
    return available

def scores ():
    score_window = tk.Tk()
    score_window.title("scoreboard")
    #score_window.attributes("-fullscreen", True)
    score_window.geometry("+0+0")
    score_window.geometry("1100x980")
    score_window.config(background='#7dbbf5')
    button3 = tk.Button(score_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[score_window.destroy(),main()])
    button3.pack()

def play ():
    data=[]
    game_window = tk.Tk()
    game_window.title("game")
    #game_window.attributes("-fullscreen", True)
    game_window.geometry("+0+0")
    game_window.geometry("1500x980")
    game_window.config(background='#7dbbf5')
    largeurCanvas, hauteurCanvas = 800, 800
    nbUnite = 10
    tailleUnite = largeurCanvas / nbUnite
    
    def cercle(x, y, rayon, color, offset): 
        offset = offset / 2
        x0 = x - rayon - offset
        y0 = y - rayon - offset
        x1 = x + rayon - offset
        y1 = y + rayon - offset
        return canvas.create_oval(x0, y0, x1, y1, fill = color)
    
    def calculeMax():
        return int(largeurCanvas/(tailleUnite * 2)), int(hauteurCanvas/(tailleUnite *
                                                                        2))
    def coo(x,y):
        return largeurCanvas/2+x*tailleUnite, hauteurCanvas/2-y*tailleUnite
    
    def initGraphique():
        for l in range(-maxy+1, maxy):
            canvas.create_line(coo(-maxx,l),coo(maxx,l), width=1, fill='black', dash=(5,3))
            canvas.create_line(coo(-maxx,0),coo(maxx,0), width=2, fill='black')
        for c in range(-maxx+1, maxx):
            canvas.create_line(coo(c,-maxy),coo(c,maxy), width=1, fill='black', dash=(5,3))
            canvas.create_line(coo(0,-maxy),coo(0,maxy), width=2, fill='black')
        val = '0'
        X = 100
        Y = 50
        for t in range (10):
            val = int(val)
            val += 1
            val = str(val)
            Y = Y + 80
            tk.Label(game_window, text=val, bg = '#7dbbf5').place(x = X, y = Y)
            tk.Label(game_window, text=val, bg = '#7dbbf5').place(x = Y + 50, y = X - 50)
            
    def add(nb):
        abscisse = int(input_X.get(1.0, "end-1c"))
        ordonnee = int(input_Y.get(1.0, "end-1c"))
        coo = [abscisse, ordonnee]
        input_Y.delete("1.0","end")
        input_X.delete("1.0","end") 
        col = 0
        for n in range(len(boats)):
            for m in range(len(boats[n])):
                if boats[n][m] == coo :
                    print("touché")
                    col = 1
                    data.append(coo)
                    if len(data)== nb:
                      victory_window = tk.Tk()
                      victory_window.title("winner")  
                      victory_window.geometry("500x500")
                      tk.Label(victory_window, text = 'bien joué vous avez gagné', height = 10).pack()
                      tk.Button(victory_window, text = 'main menu',  command=lambda:[victory_window.destroy(), game_window.destroy(),main()]).pack()
                if col == 1:    
                    color = 'red'
                elif col != 1 :
                    color = 'green'
                cercle(abscisse * tailleUnite, ordonnee * tailleUnite, 40, color, tailleUnite)
        
    def parameters(boat_parameters, x, y):
        boat_param = str(boat_parameters['quantity']) + " boats of lenght " + str(boat_parameters['lenght']) + " squares"
        param = tk.Label(game_window, text=boat_param ,bg = '#7dbbf5').place(x=x, y=y)
            
    row = 10
    collums = 10
    availablePos = available(row, collums)
    boat_parameters_1 = {
        "lenght" : 2,
        "quantity" :  1}
    boats, availablePos= boat.generate(boat_parameters_1, availablePos, row, collums)
    boat_parameters_2 = {
        "lenght" : 2,
        "quantity" :  1}
    newGen, availablePos = boat.generate(boat_parameters_2, availablePos, row, collums)
    nb_squares = (boat_parameters_1['quantity']*boat_parameters_1['lenght'] )+ (boat_parameters_2['quantity']*boat_parameters_1['lenght'])
    for t in range (boat_parameters_2['quantity']):
        boats.append(newGen[t-1]) 
    print(boats)
    parameters(boat_parameters_1, 1000, 150)
    parameters(boat_parameters_2, 1000, 200)
    tk.Label(game_window, text='the red points show the hit ships', bg = '#7dbbf5').place(x=1000, y=100)
    maxx, maxy = calculeMax()
    canvas = Canvas(game_window, width=largeurCanvas, height=hauteurCanvas, bg='grey')
    canvas.place(x=150, y= 100)
    initGraphique()
    boutonAdd = Button(game_window, text="placer bombe", command=lambda: add(nb_squares))
    boutonAdd.place(x = 650, y = 920)
    tk.Label(game_window, text='X -> ', bg = '#7dbbf5').place(x = 350, y = 920)
    input_X = Text(game_window,height = 1,width = 5)
    input_X.place(x = 400, y = 920)
    tk.Label(game_window, text='Y -> ', bg = '#7dbbf5').place(x = 500, y = 920)
    input_Y = Text(game_window,height = 1,width = 5)
    input_Y.place(x = 550, y = 920)
    #label = tk.Label(game_window, text = 'pseudo', height = 1, bg = '#7dbbf5')
    #label.place(x=500, y=900)    
    #pseudo = Text(game_window,height = 1,width = 15)
    #pseudo.place(x = 600, y = 900)
    buttonquit = tk.Button(game_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[game_window.destroy(),main()])
    buttonquit.place(x=0, y=0)

def parameters ():
    param_window = tk.Tk()
    param_window.title("param")
    #param_window.attributes("-fullscreen", True)
    param_window.geometry("+0+0")
    param_window.geometry("1100x980")
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
    main_window.geometry("1100x980")
    main_window.config(background='#7dbbf5')
    button1 = tk.Button(main_window, text="Jouer", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[main_window.destroy(),play()])
    #button2 = tk.Button(main_window, text="Score", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[main_window.destroy(),scores()])
    #button3 = tk.Button(main_window, text="parametres", font=("Courrier", 25), bg='White', fg='Black', command=lambda:[main_window.destroy(),parameters()])
    button4 = tk.Button(main_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=main_window.destroy)
    title = tk.Label(main_window, text="Battleship Game", font=("Courrier", 40), bg='#7dbbf5', fg='black')    
    title.pack(expand = True)
    button1.pack(expand=True)
    #button2.pack(expand=True)
    #button3.pack(expand=True)
    button4.pack()
    main_window.mainloop() 
    
main()
