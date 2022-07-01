'''
A game where each player throws at the numbers from 1 to 20 and bulls, counting only what they
hit on that number.
'''
import tkinter as tk
from tkinter.constants import  NSEW




class Player():
    pass



class RoundTheBoard(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Round the Board")
        #self.geometry('900x600')

        self.menu = tk.Menu(self, bg="lightgrey", fg="black")
        # first menu item
        self.game_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")
        self.game_menu.add_command(label="New Game", command=self.new_game)
        self.menu.add_cascade(label="Game Options", menu=self.game_menu)

        # second menu item
        self.stat_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")
        self.stat_menu.add_command(label="Stats", command=self.stats_window)
        self.menu.add_cascade(label="Statistics", menu=self.stat_menu)

        # populate the menu
        self.config(menu=self.menu)

        # setup main frame
        main_frame = tk.Frame(self)
        main_frame.grid(row=0, column=0, sticky=NSEW)
        player_name_label = tk.Label(main_frame, text='Angus')
        player_name_label.grid(row=0, column=0)


    def new_game(self):
        self.new_game_window = tk.Toplevel()
        player_name = tk.Label(self.new_game_window, text="Player Name")
        player_name.grid(row=0,column=0)


    def stats_window(self):
        pass


if __name__ == "__main__":
    game = RoundTheBoard()
    game.mainloop()
    