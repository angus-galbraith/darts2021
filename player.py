import game as g





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
            #player1.stats['legs'] = 0
            #player2.stats['legs'] = 0
            g.resetScores()
            g.pl1screenRefresh()
            g.pl2screenRefresh()
            g.playerToThrow()


    def gamewon(self):
        print("Game Won")

