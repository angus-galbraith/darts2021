import tkinter as tk
from tkinter.constants import BOTH, E, EW, GROOVE, LEFT, RAISED, RIGHT, TOP, TRUE, VERTICAL, W, X, Y, YES



class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Darts")
        #self.geometry('900x600')

        # create menu items 
        self.menu = tk.Menu(self, bg="lightgrey", fg="black")
        self.game_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")
        self.game_menu.add_command(label="New Game", command=self.new_game)
        #self.pack_propagate(0)
        self.menu.add_cascade(label="Game Options", menu=self.game_menu)
        self.config(menu=self.menu)

        

        # create frames
    
        
        pl1stats_frame = tk.LabelFrame(self, text='Player 1')
        pl1stats_frame.grid(row=0, column=0, sticky=EW)
        

        score_frame = tk.LabelFrame(self, text='Scores')
        score_frame.grid(row=0, column=1, sticky=EW)
        

        pl2stats_frame = tk.LabelFrame(self, text='Player 2')
        pl2stats_frame.grid(row=0, column=2, sticky=EW)

        self.grid_columnconfigure(0, weight=1, uniform='group1')
        self.grid_columnconfigure(1, weight=1, uniform='group1')
        self.grid_columnconfigure(2, weight=1, uniform='group1')


        #player1 widgets
        
        
        player1sets = tk.Label(pl1stats_frame, text="Sets:  ")
        player1sets.grid(row=0, column=0, sticky=EW)
        player1setsvalue = tk.Label(pl1stats_frame, text=" 0")
        player1setsvalue.grid(row=0, column=1, sticky=EW)
        
        player1legs = tk.Label(pl1stats_frame, text="Legs:  ")
        player1legs.grid(row=1, column=0, sticky=EW)
        player1legsvalue = tk.Label(pl1stats_frame, text=" 0")
        player1legsvalue.grid(row=1, column=1, sticky=EW)

        player1180 = tk.Label(pl1stats_frame, text="180:  ")
        player1180.grid(row=2, column=0, sticky=EW)
        player1180value = tk.Label(pl1stats_frame, text=" 0")
        player1180value.grid(row=2, column=1, sticky=EW)

        player1140 = tk.Label(pl1stats_frame, text="140+:  ")
        player1140.grid(row=3, column=0, sticky=EW)
        player1140value = tk.Label(pl1stats_frame, text=" 0")
        player1140value.grid(row=3, column=1, sticky=EW)

        player1100 = tk.Label(pl1stats_frame, text="100+:  ")
        player1100.grid(row=4, column=0, sticky=EW)
        player1100value = tk.Label(pl1stats_frame, text=" 0")
        player1100value.grid(row=4, column=1, sticky=EW)

        player180 = tk.Label(pl1stats_frame, text="80+:  ")
        player180.grid(row=5, column=0, sticky=EW)
        player180value = tk.Label(pl1stats_frame, text=" 0")
        player180value.grid(row=5, column=1, sticky=EW)

        player160 = tk.Label(pl1stats_frame, text="60+:  ")
        player160.grid(row=6, column=0, sticky=EW)
        player160value = tk.Label(pl1stats_frame, text=" 0")
        player160value.grid(row=6, column=1, sticky=EW)

        player1avge = tk.Label(pl1stats_frame, text="Average:  ")
        player1avge.grid(row=7, column=0, sticky=EW)
        player1avgevalue = tk.Label(pl1stats_frame, text=" 0")
        player1avgevalue.grid(row=7, column=1, sticky=EW)

        player1chkout = tk.Label(pl1stats_frame, text="Checkout %:  ")
        player1chkout.grid(row=8, column=0, sticky=EW)
        player1chkoutvalue = tk.Label(pl1stats_frame, text=" 0")
        player1chkoutvalue.grid(row=8, column=1, sticky=EW)

        #score frame widets

        player1_remaining = tk.Label(score_frame, text="Player 1")
        player1_remaining.grid(row=0, column=0)
        
        #player2 widgets

        player2sets = tk.Label(pl2stats_frame, text="Sets:  ")
        player2sets.grid(row=0, column=0, sticky=EW)
        player2setsvalue = tk.Label(pl2stats_frame, text=" 0")
        player2setsvalue.grid(row=0, column=1, sticky=EW)
        
        player2legs = tk.Label(pl2stats_frame, text="Legs:  ")
        player2legs.grid(row=1, column=0, sticky=EW)
        player2legsvalue = tk.Label(pl2stats_frame, text=" 0")
        player2legsvalue.grid(row=1, column=1, sticky=EW)

        player2180 = tk.Label(pl2stats_frame, text="180:  ")
        player2180.grid(row=2, column=0, sticky=EW)
        player2180value = tk.Label(pl2stats_frame, text=" 0")
        player2180value.grid(row=2, column=1, sticky=EW)

        player2140 = tk.Label(pl2stats_frame, text="140+:  ")
        player2140.grid(row=3, column=0, sticky=EW)
        player2140value = tk.Label(pl2stats_frame, text=" 0")
        player2140value.grid(row=3, column=1, sticky=EW)

        player2100 = tk.Label(pl2stats_frame, text="100+:  ")
        player2100.grid(row=4, column=0, sticky=EW)
        player2100value = tk.Label(pl2stats_frame, text=" 0")
        player2100value.grid(row=4, column=1, sticky=EW)

        player280 = tk.Label(pl2stats_frame, text="80+:  ")
        player280.grid(row=5, column=0, sticky=EW)
        player280value = tk.Label(pl2stats_frame, text=" 0")
        player280value.grid(row=5, column=1, sticky=EW)

        player260 = tk.Label(pl2stats_frame, text="60+:  ")
        player260.grid(row=6, column=0, sticky=EW)
        player260value = tk.Label(pl2stats_frame, text=" 0")
        player260value.grid(row=6, column=1, sticky=EW)

        player2avge = tk.Label(pl2stats_frame, text="Average:  ")
        player2avge.grid(row=7, column=0, sticky=EW)
        player2avgevalue = tk.Label(pl2stats_frame, text=" 0")
        player2avgevalue.grid(row=7, column=1, sticky=EW)

        player2chkout = tk.Label(pl2stats_frame, text="Checkout %:  ")
        player2chkout.grid(row=8, column=0, sticky=EW)
        player2chkoutvalue = tk.Label(pl2stats_frame, text=" 0")
        player2chkoutvalue.grid(row=8, column=1, sticky=EW)


    def new_game(self):
        pass

if __name__ == "__main__":
    screen = MainScreen()
    screen.mainloop()