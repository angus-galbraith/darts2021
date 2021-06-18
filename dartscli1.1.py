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

        self.winner = False
    

    def toThrow(self, player):
        pass

    def scoreEntered(self, player, score):
        pass
    
    def legWon(self, player):
        pass

    def setWon(self, player):
        pass
    

    def matchWon(self, player):
        pass



if __name__ == "__main__":
    g = game()
