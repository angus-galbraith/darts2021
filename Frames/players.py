



class player:
    def __init__(self,):

        self.name = "Player"
        
        self.stats = {
            "name": "Player",
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

        self.score = {
            "remaining": 501,
            "totalscore": 0,
            "totaldarts": 0,
        }

    def score_entered(self, score):
        score = score
        print(score)
        

