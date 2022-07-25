from tkinter import *
from frameimport import *
from players import player

root = Tk()
# create menus
my_menu = Menu(root)
root.config(menu=my_menu)


# create the players
player1 = player()
player2 = player()

        
# functions


def add_frames(root):
    frame_one = FrameOne(root)
    frame_one.pack(side=LEFT, expand=YES, fill=BOTH)
    frame_three = FrameThree(root)
    frame_three.pack(side=LEFT, expand=YES, fill=BOTH)
    frame_two = FrameTwo(root)
    frame_two.pack(side=LEFT, expand=YES, fill=BOTH)
    frame_one.screen_refresh(player1.stats)
    frame_two.screen_refresh(player2.stats)

def new_game_window():
    win = Toplevel()
    Label(win, text="Player 1:").grid(row=0, column=0)
    pl1ent = Entry(win)
    pl1ent.grid(row=0,column=1)
    Label(win, text="Player 2:").grid(row=1, column=0)
    pl2ent = Entry(win)
    pl2ent.grid(row=1,column=1)
    Label(win, text="Sets: First to:-").grid(row=2, column=0)
    sets_spinbox = Spinbox(win, values=(1,2,3,4))
    sets_spinbox.grid(row=2, column=1)
    Label(win, text="Legs: First to:-").grid(row=3, column=0)
    legs_spinbox = Spinbox(win, values=(1,2,3,4))
    legs_spinbox.grid(row=3, column=1)
    Button(win, text="Start", command=lambda: start_game(win)).grid(row=4, column=1,columnspan=2)

def start_game(win):
    win.destroy()


options_menu= Menu(my_menu)
my_menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='New Game', command=new_game_window)


# add_frames(root)
root.mainloop()