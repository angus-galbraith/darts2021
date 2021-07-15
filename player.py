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
        self.stats['legs'] += 1
        

        
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
        
        if self.stats['legs'] == g.legstowin:
            self.setwon()


        
        

        return

    def setwon(self):
        pass

