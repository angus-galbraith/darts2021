from player import player as player1
from player import player as player2
from dartstk1_2 import MainScreen as screen


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


