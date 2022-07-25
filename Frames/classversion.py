from tkinter import *
from frameimport import *
from players import player

root = Tk()
root.title("Darts")
root.geometry("600x600")


class gameLoop:

    def __init__(self, master):
        self.game_frame = Frame(master)
        self.game_frame.pack()

        # Create Menus 
        self.my_menu = Menu(root)
        root.config(menu=self.my_menu)
        self.options_menu= Menu(self.my_menu)
        self.my_menu.add_cascade(label='Options', menu=self.options_menu) 
        self.options_menu.add_command(label='New Game', command=self.new_game_window)

        self.add_frames()


    def add_frames(self):
       self.frame_one = scoreFrame(self.game_frame)
       self.frame_one.pack(side=LEFT, expand=YES, fill=BOTH)
       self.frame_three = scoreFrame(self.game_frame)
       self.frame_three.pack(side=LEFT, expand=YES, fill=BOTH)
       self.frame_two = scoreFrame(self.game_frame)
       self.frame_two.pack(side=LEFT, expand=YES, fill=BOTH)
       

    def new_game_window(self):
        self.win = Toplevel()
        Label(self.win, text="Player 1:").grid(row=0, column=0)
        self.pl1ent = Entry(self.win)
        self.pl1ent.grid(row=0,column=1)
        Label(self.win, text="Player 2:").grid(row=1, column=0)
        self.pl2ent = Entry(self.win)
        self.pl2ent.grid(row=1,column=1)
        Label(self.win, text="Sets: First to:-").grid(row=2, column=0)
        self.sets_spinbox = Spinbox(self.win, values=(1,2,3,4))
        self.sets_spinbox.grid(row=2, column=1)
        Label(self.win, text="Legs: First to:-").grid(row=3, column=0)
        self.legs_spinbox = Spinbox(self.win, values=(1,2,3,4))
        self.legs_spinbox.grid(row=3, column=1)
        Button(self.win, text="Start", command=self.start_game).grid(row=4, column=1,columnspan=2)

    def start_game(self):
        player1 = player()
        player2 = player()
        player1.stats["name"] = self.pl1ent.get()
        player2.stats["name"] = self.pl2ent.get()
        self.frame_one.screen_refresh(player1.stats)
        self.frame_two.screen_refresh(player2.stats)
        self.frame_three.screen_setup(player1.stats, player2.stats)
        self.legs_to_win = self.legs_spinbox.get()
        self.sets_to_win = self.sets_spinbox.get()
        self.to_throw()
        self.win.destroy()

    def to_throw(self):
        pass

game = gameLoop(root)
root.mainloop()