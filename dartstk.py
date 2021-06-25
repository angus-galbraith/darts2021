import tkinter as tk
from tkinter.constants import BOTH, GROOVE, VERTICAL, Y



class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Darts")
        self.geometry('800x600')

        # create menu items 
        self.menu = tk.Menu(self, bg="lightgrey", fg="black")
        self.game_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")
        self.game_menu.add_command(label="New Game", command=self.new_game)

        self.menu.add_cascade(label="Game Options", menu=self.game_menu)
        self.config(menu=self.menu)

        

        # create frames
        name_frame = tk.Frame(self, background='blue', relief=GROOVE)
        name_frame.pack(side=tk.TOP, fill=BOTH)
        
        pl1stats_frame = tk.Frame(self, background='red')
        pl1stats_frame.pack(side=tk.LEFT, fill=BOTH)
        pl1sets_label = tk.Label(pl1stats_frame, text='Sets')
        pl1sets_label.pack()

        score_frame = tk.Frame(self, background='yellow')
        score_frame.pack(side=tk.LEFT, fill=BOTH)
        score_label = tk.Label(score_frame, text='remaining')
        score_label.pack()

        #pl2stats_frame = tk.Frame(self, background='red')
        #pl2stats_frame.pack(side=tk.LEFT, fill=BOTH)

    def new_game(self):
        pass

if __name__ == "__main__":
    screen = MainScreen()
    screen.mainloop()