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
        self.playerToThrow(1)

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
        print("Current Score : ")
        print("Player 1 Sets ", self.player1.stats['sets'], "Legs ", self.player1.stats['legs'])
        print("Player 2 Sets ", self.player2.stats['sets'], "Legs ", self.player2.stats['legs'])
        if player == 1:
            print(self.player1.stats['name'], "to go you have ", self.player1.stats['score'], "remaining")
            self.scoreEntered(1)

        else:
            print(self.player2.stats['name'], "to go you have ", self.player2.stats['score'], "remaining")
            self.scoreEntered(2)
        

    def scoreEntered(self, player):
        if player == 1:
            score = int(input("Enter Score : - "))
            newScore = self.player1.stats['score'] - score
            self.player1.stats['score'] = newScore
            if newScore == 0:
                self.legWon(1)
            else:
                self.toThrow(2)

        else:
            score = int(input("Enter Score : - "))
            newScore = self.player2.stats['score'] - score
            self.player2.stats['score'] = newScore
            if newScore == 0:
                self.legWon(2)
            else:
                self.toThrow(1)
        

    def legWon(self, player):
        if player == 1:
            self.player1.stats['legs']+= 1
            if self.player1.stats['legs'] == self.gameState['legstowin']:
                self.setWon(1)
            else:
                self.player1.stats['score'] = 501
                self.player2.stats['score'] = 501
                self.legToPlay += 1
                self.playerToThrow()
                

        else:
            self.player2.stats['legs']+= 1
            if self.player2.stats['legs'] == self.gameState['legstowin']:
                self.player2.stats['sets']+= 1
                self.setWon(2)
            else:
                self.player1.stats['score'] = 501
                self.player2.stats['score'] = 501
                self.legToPlay += 1
                self.playerToThrow()



    def setWon(self, player):
        if player == 1:
            self.player1.stats['sets']+= 1
            if self.player1.stats['sets'] == self.gameState['setstowin']:
                self.matchWon(1)
            else:
                self.player1.stats['score'] = 501
                self.player2.stats['score'] = 501
                self.legToPlay = 1
                self.playerToThrow()
        
        else:
            self.player2.stats['sets']+= 1
            if self.player2.stats['sets'] == self.gameState['setstowin']:
                self.matchWon(2)
            else:
                self.player1.stats['score'] = 501
                self.player2.stats['score'] = 501
                self.playerToThrow()


    

    def matchWon(self, player):
        pass



if __name__ == "__main__":
    g = game()
