'''
A game where each player throws at the numbers from 1 to 20 and bulls, counting only what they
hit on that number.
'''
import tkinter as tk




class Player():
    pass



class RoundTheBoard(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Round the Board")
        #self.geometry('900x600')


        self.menu = tk.Menu(self, bg="lightgrey", fg="black")
        self.game_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")
        self.game_menu.add_command(label="New Game", command=self.new_game)
        #self.pack_propagate(0)
        self.menu.add_cascade(label="Game Options", menu=self.game_menu)
        self.config(menu=self.menu)

    def new_game(self):
        pass

    
if __name__ == "__main__":
    game = RoundTheBoard()
    game.mainloop()
    