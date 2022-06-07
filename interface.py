#mes bateaux en bleu
#mes bateaux touchés en rouge 
#mes mines non touchés en vert
#mes mines touchés en orange 

import tkinter as tk

def scores ():
    score_window = tk.Tk()
    score_window.title("scoreboard")
    score_window.attributes("-fullscreen", True)
    score_window.config(background='#7dbbf5')
    button3 = tk.Button(score_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=score_window.destroy)
    button3.pack()

def play ():
    game_window = tk.Tk()
    game_window.title("game")
    game_window.attributes("-fullscreen", True)
    game_window.config(background='#7dbbf5')
    button3 = tk.Button(game_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=game_window.destroy)
    button3.pack()

def parameters ():
    param_window = tk.Tk()
    param_window.title("param")
    param_window.attributes("-fullscreen", True)
    param_window.config(background='#6b6e6c')
    button3 = tk.Button(param_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=param_window.destroy)
    button3.pack()

main_window = tk.Tk()
main_window.title("Battleship")
main_window.attributes("-fullscreen", True)
main_window.config(background='#7dbbf5')
button1 = tk.Button(main_window, text="Jouer", font=("Courrier", 25), bg='White', fg='Black', command=lambda:play())
button2 = tk.Button(main_window, text="Score", font=("Courrier", 25), bg='White', fg='Black', command=lambda:scores())
button3 = tk.Button(main_window, text="parametres", font=("Courrier", 25), bg='White', fg='Black', command=lambda:parameters())
button4 = tk.Button(main_window, text="quit", font=("Courrier", 25), bg='White', fg='Black', command=main_window.destroy)
title = tk.Label(main_window, text="Battleship Game", font=("Courrier", 40), bg='#7dbbf5', fg='black')

title.pack(expand = True)
button1.pack(expand=True)
button2.pack(expand=True)
button3.pack(expand=True)
button4.pack()
main_window.mainloop() 