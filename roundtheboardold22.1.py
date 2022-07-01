from tkinter import*
import os


class MainApplication(Frame):

    

    def __init__(self, master):
        self.master = master
        Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()


    def configure_gui(self):
        self.master.title("Round The Board")
        self.master.geometry("300x100")
        self.highScoreCheck()
        


    def create_widgets(self):

        self.master.bind('<Return>',lambda e:self.scoreEntered())


        #Variables
        self.numberToGoFor = StringVar()
        self.numberHit = StringVar()
        self.player_name = StringVar()
        self.playerName = StringVar()
        self.runningTotal = StringVar()
        self.gameOverPlayer = StringVar()
        self.highest_score = StringVar()
        self.high_score_table = StringVar()
        self.highScoreTable1 = StringVar()
        self.highScoreTable2 = StringVar()
        self.highScoreTable3 = StringVar()
        self.highScoreTable4 = StringVar()
        self.highScoreTable5 = StringVar()
        self.highScoreTable6 = StringVar()
        self.highScoreTable7 = StringVar()
        self.highScoreTable8 = StringVar()
        self.highScoreTable9 = StringVar()
        self.highScoreTable10 = StringVar()
        
        #Widgets

        ##row0
        name_label = Label(self.master, text="Player")
        name_label.grid(row=0, column=0, sticky=W)
        name_label2 = Label(self.master, textvariable=self.player_name)
        name_label2.grid(row=0,column=1, sticky=E)
        #row1
        number_to_go_for = Label(self.master, text="Number to go for:")
        number_to_go_for.grid(row=1,column=0, sticky=W)
        number_hit = Label(self.master, text="How Many Hit")
        number_hit.grid(row=1,column=1, sticky=E)
        running_total = Label(self.master, text="Running Total")
        running_total.grid(row=1,column=2, sticky=E)
        #row2
        number_label = Label(self.master, textvariable=self.numberToGoFor)
        number_label.grid(row=2, column=0, sticky=EW)
        self.number_entry = Entry(self.master, textvariable=self.numberHit, width=5)
        self.number_entry.grid(row=2, column=1)
        sub_total = Label(self.master, textvariable=self.runningTotal)
        sub_total.grid(row=2, column=2)
        #row3
        new_game = Button(self.master, text="New Game", command=self.newGame)
        new_game.grid(row=3, column=0)
        view_stats = Button(self.master, text="View Stats", command=self.viewStats)
        view_stats.grid(row=3, column=1)
        high_score = Label(self.master, textvariable=self.highest_score)
        high_score.grid(row=3, column=2)

        #Functions

    def newGame(self):
        self.new_game_window = Toplevel(self.master)
        player_name = Label(self.new_game_window, text="Players Name:")
        player_name.grid(row=0, column=0)
        name_entry = Entry(self.new_game_window, textvariable=self.playerName)
        name_entry.grid(row=0, column=1)
        start_button = Button(self.new_game_window, text="Start Game", command=self.startGame)
        start_button.grid(row=1, column=0, columnspan=2, sticky=W)
                 
    def viewStats(self):
        self.view_stats_window = Toplevel(self.master)
        Button(self.view_stats_window, text="High Scores", command=self.highScores).grid(row=0, column=0)
        Button(self.view_stats_window, text="Player Stats", command=self.playerStats).grid(row=0, column=1)



    def highScores(self):
        pass


    
    


        
    
            

        


    def startGame(self):
        self.new_game_window.destroy()
        self.playerName = self.playerName.get()
        self.player_name.set(self.playerName)
        # self.playerStats(self.playerName)
        self.number_entry.focus()
        self.number_to_go_for = 1
        self.total = 0
        self.numberToGoFor.set(self.number_to_go_for)
        self.runningTotal.set(0)
        self.highest_score.set(self.highestScore)
        
    
        

    def scoreEntered(self):
        self.number_entered = int(self.numberHit.get())
    
        self.throw_total = self.number_entered * self.number_to_go_for
        self.total += self.throw_total
        self.runningTotal.set(self.total)
        self.number_to_go_for += 1
        if self.number_to_go_for == 21:
            self.number_to_go_for = "Bulls "
            self.numberToGoFor.set(self.number_to_go_for)
            self.numberHit.set("")
            self.number_to_go_for = 25
        else:
            self.numberToGoFor.set(self.number_to_go_for)
            self.numberHit.set("")
        if self.number_to_go_for ==26:
            self.game_over(self.total)
            
        #self.numberToGoFor.set(self.number_to_go_for)
        #self.numberHit.set("")

    def game_over(self,final_total):
        self.game_over_window = Toplevel(self.master)
        self.game_over_window.geometry("200x100")
        #row0
        game_over_player = Label(self.game_over_window, textvariable=self.gameOverPlayer)
        game_over_player.grid(row=0, column=0)
        display_message = ("%s Scored: %s " % (self.playerName, final_total))
        self.gameOverPlayer.set(display_message)
        self.highScoreTable(final_total, self.playerName,  self.highestScoreTable)
        if final_total > self.highestScore:
            self.resetHighScore(final_total, self.playerName, self.highestScoreTable)
        print("Total", final_total)






    
if __name__=='__main__':
    root = Tk()
    main_app = MainApplication(root)
    
    root.mainloop()
