




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
        self.sets = input("Number of Sets: ")
        self.legs = input("Number of Legs per Set: ")
        self.gameState = {
            "sets": self.sets,
            "legs": self.legs,
            "playerToGo": 1,

        }

        self.winner = False
        self.startGame()





    def startGame(self):

    
        
        while self.winner == False:
            if self.gameState['playerToGo'] == 1:
                print(self.player1.stats['name'], "to go you have ", self.player1.stats['score'], "remaining")
                self.score = int(input("Enter Score:"))
                oldScore = int(self.player1.stats['score'])
                newScore = oldScore - self.score
                self.player1.stats['score'] = newScore
                if newScore == 0:
                    self.legWon(1)
                else:
                    print(self.player1.stats['score'])
                    self.gameState['playerToGo'] = 2
                
            else:
                print(self.player2.stats['name'], "to go you have ", self.player2.stats['score'], "remaining")
                self.score2= int(input("Enter Score:"))
                oldScore = int(self.player2.stats['score'])
                newScore = oldScore - self.score2
                self.player2.stats['score'] = newScore
                if newScore == 0:
                    self.legWon(2)
                else:
                    print(self.player2.stats['score'])
                    self.gameState['playerToGo'] = 1
            
                

    def legWon(self, player):
        
        if player == 1:
            print("Player 1 won that leg.")
            self.player1.stats['legs'] += 1
            print(print(self.player1.stats['legs']))
            self.winner = True

        else:
            print("Player 2 won that leg.")
            self.winner = True




    

        


        


        



    

    





if __name__ == "__main__":
    g = game()
