from tkinter import *




class FrameOne(Frame):

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



class FrameTwo(Frame):

    def __init__(self, parent=None, **options):
        
        LabelFrame.__init__(self, parent, **options)
        self.pack()
        
    def screen_refresh(self, player):
        self.player2 = player
        rownum = 0
        for (key, value) in self.player2.items():
            Label(self, text=key).grid(row=rownum, column=0)
            Label(self, text=value).grid(row=rownum, column=1)
            rownum += 1

class FrameThree(Frame):

    def __init__(self, parent=None, **options):
        
        LabelFrame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="scores Frame").pack()

if __name__ =='__main__':
    FrameOne().mainloop()
        