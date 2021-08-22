import tkinter as tk
from tkinter.constants import BOTH, E, EW, GROOVE, LEFT, NSEW, RAISED, RIGHT, TOP, TRUE, VERTICAL, W, X, Y, YES

class player:
    def __init__(self,):
        
        self.stats = {
            "name": "Player",
            "score": 501,
            "sets": 0,
            "legs": 0,
            "180": 0,
            "140": 0,
            "100": 0,
            "80": 0,
            "60": 0,
            "Average": 0,
            "Checkout %": 0,
            "totalscore": 0,
            "totaldarts": 0,
        }
        
    def scoreEntered(self, score):
        score=score
        newScore = self.stats['score'] - score
        self.stats['score'] = newScore
        self.stats['totalscore'] += score
        self.stats['totaldarts'] += 3
        self.stats["Average"] = (self.stats['totalscore']/self.stats['totaldarts']) * 3
        
        

        
        if score == 180:
            self.stats['180'] += 1
        elif score >= 140:
            self.stats['140'] += 1
        elif score >= 100:
            self.stats['100'] += 1
        elif score >= 80:
            self.stats['80'] += 1
        elif score >= 60:
            self.stats['60'] += 1
        
        if self.stats['score'] == 0:
            self.legwon()
        

        return

    def legwon(self):
        self.stats['legs'] += 1
        print(g.legstowin)

        if self.stats['legs'] == g.legstowin:
            self.setwon()

        else:
            g.resetScores()
            g.pl1screenRefresh()
            g.pl2screenRefresh()
            g.legToPlay += 1
            g.playerToThrow()
            






    def setwon(self):
        self.stats['sets'] += 1
        if self.stats['sets'] == g.setstowin:
            self.gamewon
        else:
            g.setstowin += 1
            player1.stats['legs'] = 0
            player2.stats['legs'] = 0
            g.resetScores()
            g.pl1screenRefresh()
            g.pl2screenRefresh()
            g.playerToThrow()


    def gamewon(self):
        print("Game Won")


class game:
    def __init__(self):
        pass
    


    def gameStatus(self, sets, legs):
        self.setstowin = sets//2 + 1
        self.legstowin = legs//2 + 1
        self.legToPlay = 1
        self.setToPlay = 1
        self.to_throw = 1
        self.currentPlayer = 0
        self.winner = False
        screen.player1name.set(player1.stats["name"])
        screen.player2name.set(player2.stats["name"])
        

    def playerToThrow(self):
        if self.setToPlay % 2 != 0:
            if self.legToPlay % 2 != 0:
                self.currentPlayer = 1
                self.toThrow()
            else:
                self.currentPlayer = 2
                self.toThrow()
        else:
            if self.legToPlay % 2 != 0:
                self.currentPlayer = 2
                self.toThrow()
            else:
                self.currentPlayer = 1
                self.toThrow()

    def toThrow(self):
        
        if self.currentPlayer == 1:
            screen.player1remaining_label.configure(bg="yellow")
            screen.player2remaining_label.configure(bg="white")
            screen.playertothrow.set(player1.stats["name"])
            screen.score_entry.focus()
            
            

        else:
            screen.player2remaining_label.configure(bg="yellow")
            screen.player1remaining_label.configure(bg="white")
            screen.playertothrow.set(player2.stats["name"])
            



    def buttonPressed(self, score):
        
        if self.currentPlayer == 1:
            player1.scoreEntered(score)
            screen.score_entry.delete(0, 'end')
            self.pl1screenRefresh()
            self.currentPlayer = 2
            self.toThrow()

        else:
            player2.scoreEntered(score)
            screen.score_entry.delete(0, 'end')
            self.pl2screenRefresh()
            self.currentPlayer = 1
            self.toThrow()

    def pl1screenRefresh(self):
        screen.player1sets.set(player1.stats['sets'])
        screen.player1legs.set(player1.stats['legs'])
        screen.player1remaining.set(player1.stats['score'])
        screen.player1_180.set(player1.stats['180'])
        screen.player1_140.set(player1.stats['140'])
        screen.player1_100.set(player1.stats['100'])
        screen.player1_80.set(player1.stats['80'])
        screen.player1_60.set(player1.stats['60'])
        screen.player1avge.set(player1.stats['Average'])

    def pl2screenRefresh(self):
        screen.player2sets.set(player2.stats['sets'])
        screen.player2legs.set(player2.stats['legs'])
        screen.player2remaining.set(player2.stats['score'])
        screen.player2_180.set(player2.stats['180'])
        screen.player2_140.set(player2.stats['140'])
        screen.player2_100.set(player2.stats['100'])
        screen.player2_80.set(player2.stats['80'])
        screen.player2_60.set(player2.stats['60'])
        screen.player2avge.set(player2.stats['Average'])


    def resetScores(self):
        player1.stats['score'] = 501
        player2.stats['score'] = 501

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

        #variables 
        self.player1name = tk.StringVar()
        self.player1sets = tk.IntVar()
        self.player1legs = tk.IntVar()
        self.player1_180 = tk.IntVar()
        self.player1_180.set(player1.stats["180"])
        self.player1_140 = tk.IntVar()
        self.player1_100 = tk.IntVar()
        self.player1_80 = tk.IntVar()
        self.player1_60 = tk.IntVar()
        self.player1avge = tk.IntVar()
        self.player1chkout = tk.IntVar()
        self.player1remaining = tk.IntVar()
        self.player1remaining.set(player1.stats["score"])

        self.player2name = tk.StringVar()
        self.player2sets = tk.IntVar()
        self.player2legs = tk.IntVar()
        self.player2_180 = tk.IntVar()
        self.player2_140 = tk.IntVar()
        self.player2_100 = tk.IntVar()
        self.player2_80 = tk.IntVar()
        self.player2_60 = tk.IntVar()
        self.player2avge = tk.IntVar()
        self.player2chkout = tk.IntVar()
        self.player2remaining= tk.IntVar()
        self.player2remaining.set(player2.stats["score"])

        self.playertothrow = tk.StringVar()

        

        
        # create frames
    
        
        pl1stats_frame = tk.LabelFrame(self, text='Player 1')
        pl1stats_frame.grid(row=0, column=0, sticky=NSEW)
        

        score_frame = tk.LabelFrame(self, text='Scores')
        score_frame.grid(row=0, column=1, sticky=NSEW)
        

        pl2stats_frame = tk.LabelFrame(self, text='Player 2')
        pl2stats_frame.grid(row=0, column=2, sticky=NSEW)

        self.grid_columnconfigure(0, weight=1, uniform='group1')
        self.grid_columnconfigure(1, weight=1, uniform='group1')
        self.grid_columnconfigure(2, weight=1, uniform='group1')
        self.grid_rowconfigure(0, weight=1)

        


        #player1 widgets
        
        
        player1sets = tk.Label(pl1stats_frame, text="Sets:  ")
        player1sets.grid(row=0, column=0, sticky=EW)
        player1setsvalue = tk.Label(pl1stats_frame, textvariable=self.player1sets)
        player1setsvalue.grid(row=0, column=1, sticky=EW)
        
        player1legs = tk.Label(pl1stats_frame, text="Legs:  ")
        player1legs.grid(row=1, column=0, sticky=EW)
        player1legsvalue = tk.Label(pl1stats_frame, textvariable=self.player1legs)
        player1legsvalue.grid(row=1, column=1, sticky=EW)

        player1180 = tk.Label(pl1stats_frame, text="180:  ")
        player1180.grid(row=2, column=0, sticky=EW)
        player1180value = tk.Label(pl1stats_frame, textvariable=self.player1_180)
        player1180value.grid(row=2, column=1, sticky=EW)

        player1140 = tk.Label(pl1stats_frame, text="140+:  ")
        player1140.grid(row=3, column=0, sticky=EW)
        player1140value = tk.Label(pl1stats_frame, textvariable=self.player1_140)
        player1140value.grid(row=3, column=1, sticky=EW)

        player1100 = tk.Label(pl1stats_frame, text="100+:  ")
        player1100.grid(row=4, column=0, sticky=EW)
        player1100value = tk.Label(pl1stats_frame, textvariable=self.player1_100)
        player1100value.grid(row=4, column=1, sticky=EW)

        player180 = tk.Label(pl1stats_frame, text="80+:  ")
        player180.grid(row=5, column=0, sticky=EW)
        player180value = tk.Label(pl1stats_frame, textvariable=self.player1_80)
        player180value.grid(row=5, column=1, sticky=EW)

        player160 = tk.Label(pl1stats_frame, text="60+:  ")
        player160.grid(row=6, column=0, sticky=EW)
        player160value = tk.Label(pl1stats_frame, textvariable=self.player1_60)
        player160value.grid(row=6, column=1, sticky=EW)

        player1avge = tk.Label(pl1stats_frame, text="Average:  ")
        player1avge.grid(row=7, column=0, sticky=EW)
        player1avgevalue = tk.Label(pl1stats_frame, textvariable=self.player1avge)
        player1avgevalue.grid(row=7, column=1, sticky=EW)

        player1chkout = tk.Label(pl1stats_frame, text="Checkout %:  ")
        player1chkout.grid(row=8, column=0, sticky=EW)
        player1chkoutvalue = tk.Label(pl1stats_frame, textvariable=self.player1chkout)
        player1chkoutvalue.grid(row=8, column=1, sticky=EW)

        #score frame widets

        player1_remaining = tk.Label(score_frame, text="Remaining")
        player1_remaining.grid(row=0, column=0, columnspan=2, sticky=EW)
        player1_name = tk.Label(score_frame, textvariable=self.player1name)
        player1_name.grid(row=1, column=0, sticky=EW)
        player2_name = tk.Label(score_frame, textvariable=self.player2name)
        player2_name.grid(row=1, column=1, sticky=EW)
        self.player1remaining_label = tk.Label(score_frame, textvariable=self.player1remaining, font=(None, 40))
        self.player1remaining_label.grid(row=2, column=0, sticky=NSEW)
        #self.player1remaining_label.configure(bg="yellow")
        self.player2remaining_label = tk.Label(score_frame, textvariable=self.player2remaining, font=(None, 40))
        self.player2remaining_label.grid(row=2, column=1, sticky=NSEW)
        tothrow_label = tk.Label(score_frame, text="To Throw: ")
        tothrow_label.grid(row=3, column=0)
        playertothrow_label = tk.Label(score_frame, textvariable=self.playertothrow)
        playertothrow_label.grid(row=3, column=1)
        self.score_entry = tk.Entry(score_frame, width=10)
        self.score_entry.grid(row=4, column=0)
        score_button = tk.Button(score_frame, text="Enter", command=self.buttonPressed)
        score_button.grid(row=4, column=1)



        #player2 widgets

        player2sets = tk.Label(pl2stats_frame, text="Sets:  ")
        player2sets.grid(row=0, column=0, sticky=EW)
        player2setsvalue = tk.Label(pl2stats_frame, textvariable=self.player2sets)
        player2setsvalue.grid(row=0, column=1, sticky=EW)
        
        player2legs = tk.Label(pl2stats_frame, text="Legs:  ")
        player2legs.grid(row=1, column=0, sticky=EW)
        player2legsvalue = tk.Label(pl2stats_frame, textvariable=self.player2legs)
        player2legsvalue.grid(row=1, column=1, sticky=EW)

        player2180 = tk.Label(pl2stats_frame, text="180:  ")
        player2180.grid(row=2, column=0, sticky=EW)
        player2180value = tk.Label(pl2stats_frame, textvariable=self.player2_180)
        player2180value.grid(row=2, column=1, sticky=EW)

        player2140 = tk.Label(pl2stats_frame, text="140+:  ")
        player2140.grid(row=3, column=0, sticky=EW)
        player2140value = tk.Label(pl2stats_frame, textvariable=self.player2_140)
        player2140value.grid(row=3, column=1, sticky=EW)

        player2100 = tk.Label(pl2stats_frame, text="100+:  ")
        player2100.grid(row=4, column=0, sticky=EW)
        player2100value = tk.Label(pl2stats_frame, textvariable=self.player2_100)
        player2100value.grid(row=4, column=1, sticky=EW)

        player280 = tk.Label(pl2stats_frame, text="80+:  ")
        player280.grid(row=5, column=0, sticky=EW)
        player280value = tk.Label(pl2stats_frame, textvariable=self.player2_80)
        player280value.grid(row=5, column=1, sticky=EW)

        player260 = tk.Label(pl2stats_frame, text="60+:  ")
        player260.grid(row=6, column=0, sticky=EW)
        player260value = tk.Label(pl2stats_frame, textvariable=self.player2_60)
        player260value.grid(row=6, column=1, sticky=EW)

        player2avge = tk.Label(pl2stats_frame, text="Average:  ")
        player2avge.grid(row=7, column=0, sticky=EW)
        player2avgevalue = tk.Label(pl2stats_frame, textvariable=self.player2avge)
        player2avgevalue.grid(row=7, column=1, sticky=EW)

        player2chkout = tk.Label(pl2stats_frame, text="Checkout %:  ")
        player2chkout.grid(row=8, column=0, sticky=EW)
        player2chkoutvalue = tk.Label(pl2stats_frame, textvariable=self.player2chkout)
        player2chkoutvalue.grid(row=8, column=1, sticky=EW)


    def new_game(self):
        self.newgame_window = tk.Toplevel()
        pl1_name = tk.Label(self.newgame_window, text="Player 1")
        pl1_name.grid(row=0,column=0)
        self.pl1_entry = tk.Entry(self.newgame_window)
        self.pl1_entry.grid(row=0, column=1)
        pl2_name = tk.Label(self.newgame_window, text="Player 2")
        pl2_name.grid(row=1,column=0)
        self.pl2_entry = tk.Entry(self.newgame_window)
        self.pl2_entry.grid(row=1, column=1)
        sets_label = tk.Label(self.newgame_window, text="Number of Sets.")
        sets_label.grid(row=2, column=0)
        self.sets_spinbox = tk.Spinbox(self.newgame_window, values=(1,3,5))
        self.sets_spinbox.grid(row=2, column=1)
        legs_label = tk.Label(self.newgame_window, text="Number of Legs.")
        legs_label.grid(row=3, column=0)
        self.legs_spinbox = tk.Spinbox(self.newgame_window, values=(1,3,5))
        self.legs_spinbox.grid(row=3, column=1)
        start_button = tk.Button(self.newgame_window, text="Start", command=self.start_game)
        start_button.grid(row=4, column=0, columnspan=2, sticky=EW)

    def start_game(self):
        player1.stats["name"] = self.pl1_entry.get()
        player2.stats["name"] = self.pl2_entry.get()
        sets = int(self.sets_spinbox.get())
        legs = int(self.legs_spinbox.get())
        g.gameStatus(sets, legs)
        g.playerToThrow()
        self.newgame_window.destroy()
    

    def buttonPressed(self):
        score = int(self.score_entry.get())
        g.buttonPressed(score)
        print(g.currentPlayer, score)
 
if __name__ == "__main__":
    player1 = player()
    player2 = player()
    g = game()
    screen = MainScreen()
    screen.mainloop()