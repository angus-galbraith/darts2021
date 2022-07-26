from tkinter import *




class scoreFrame(Frame):

    def __init__(self, parent=None, **options):
        LabelFrame.__init__(self, parent, **options)
        self.pack()
        

    def screen_refresh(self, player):
        self.player1 = player
        rownum = 0
        for (key, value) in self.player1.items():
            Label(self, text=key).grid(row=rownum, column=0)
            Label(self, text=value).grid(row=rownum, column=1)
            rownum += 1

    def screen_setup(self, player1, player2, player1score, player2score):
        self.player1 = player1
        self.player2 = player2
        self.pl1 =player1score
        self.pl2 =player2score
        Label(self, text=self.player1["name"], font=(None, 25)).grid(row=0, column=0)
        Label(self, text=self.player2["name"], font=(None, 25)).grid(row=0, column=1)
        self.pl1_remaining = Label(self, text=self.pl1["remaining"], font=(None, 40))
        self.pl1_remaining.grid(row=1, column=0)
        self.pl1_remaining.configure(bg="white")
        self.pl2_remaining = Label(self, text=self.pl2["remaining"], font=(None, 40))
        self.pl2_remaining.grid(row=1, column=1)
        self.pl2_remaining.configure(bg="white")
        self.score_ent = Entry(self, width=10)
        self.score_ent.grid(row=2,column=0)
        Button(self, text="Enter Score", command=self.button_pressed).grid(row=2, column=1)


    def button_pressed(self):
        pass



        