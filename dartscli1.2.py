# create a player class

class player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            "name": self.name,
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
        }

    def score_entered(self, next):
        next = next
        score = int(input("Enter Score : - "))
        newScore = self.stats['score'] - score
        self.stats['score'] = newScore
        if score == 180:
            self.stats['180'] += 1
        elif score >= 140:
            self.stats['140'] += 1
        elif score >= 140:
            self.stats['100'] += 1
        elif score >= 80:
            self.stats['80'] += 1
        elif score >= 60:
            self.stats['60'] += 1

        if newScore == 0:
            self.leg_won(1)
        else:
            g.toThrow(next)


    def leg_won(self):
        print("leg won")

    def set_won(self):
        pass

    def match_won(self):
        pass


class game:
    def __init__(self):
        # setup players
        player1name = input('Player 1: ')
        self.player1 = player(player1name)
        player2name = input('Player 2: ')
        self.player2 = player(player2name)
    
        # set game parameters
        sets = int(input("Number of Sets: "))
        legs = int(input("Number of Legs per Set: "))
        setstowin = sets//2 + 1
        legstowin = legs//2 + 1
        self.gameState = {
            "setstowin": setstowin,
            "legstowin": legstowin,
            "playerToGo": 1,

        }
        self.legToPlay = 1
        self.setToPlay = 1
        self.winner = False
        


    def playerToThrow(self):
        if self.setToPlay % 2 != 0:
            if self.legToPlay % 2 != 0:
                self.toThrow(1)
            else:
                self.toThrow(2)
        else:
            if self.legToPlay % 2 != 0:
                self.toThrow(2)
            else:
                self.toThrow(1)

    def toThrow(self, player):
        
        if player == 1:
            print(self.player1.stats['name'], "to go you have ", self.player1.stats['score'], "remaining")
            self.player1.score_entered(2)

        else:
            print(self.player2.stats['name'], "to go you have ", self.player2.stats['score'], "remaining")
            self.player2.score_entered(1)
        

    
            
        

    def legWon(self, player):
        if player == 1:
            self.player1.stats['legs']+= 1
            if self.player1.stats['legs'] == self.gameState['legstowin']:
                self.setWon(1)
            else:
                self.player1.stats['score'] = 501
                self.player2.stats['score'] = 501
                self.legToPlay += 1
                self.currentScore()
                self.playerToThrow()
                
                

        else:
            self.player2.stats['legs']+= 1
            if self.player2.stats['legs'] == self.gameState['legstowin']:
                self.setWon(2)
            else:
                self.player1.stats['score'] = 501
                self.player2.stats['score'] = 501
                self.legToPlay += 1
                self.currentScore()
                self.playerToThrow()



    def setWon(self, player):
        if player == 1:
            self.player1.stats['sets']+= 1
            if self.player1.stats['sets'] == self.gameState['setstowin']:
                self.matchWon(1)
            else:
                self.setToPlay += 1
                self.player1.stats['score'] = 501
                self.player2.stats['score'] = 501
                self.player1.stats['legs'] = 0
                self.player2.stats['legs'] = 0
                self.legToPlay = 1
                self.currentScore()
                self.playerToThrow()
        
        else:
            self.player2.stats['sets']+= 1
            if self.player2.stats['sets'] == self.gameState['setstowin']:
                self.matchWon(2)
            else:
                self.setToPlay += 1
                self.player1.stats['score'] = 501
                self.player2.stats['score'] = 501
                self.player1.stats['legs'] = 0
                self.player2.stats['legs'] = 0
                self.legToPlay = 1
                self.currentScore()
                self.playerToThrow()



    

    def matchWon(self, player):
        print("Winner")

    def currentScore(self):
        print("Current Score : ")
        print(self.player1.stats['name'], "Sets ", self.player1.stats['sets'], "Legs ", self.player1.stats['legs'])
        print(self.player2.stats['name'], "Sets ", self.player2.stats['sets'], "Legs ", self.player2.stats['legs'])
        print(self.player1.stats['180'])
        print(self.player1.stats['140'] )



if __name__ == "__main__":
    g = game()
    g.playerToThrow()
