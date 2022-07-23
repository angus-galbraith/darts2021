from tkinter import *
from frameimport import *
from players import player

root = Tk()
# create menus
my_menu = Menu(root)
root.config(menu=my_menu)





# create the players
player1 = player()
player2 = player()
player1.stats['name'] = "Angus"
        

def add_frames(root):
    frame_one = FrameOne(root)
    frame_one.pack(side=LEFT, expand=YES, fill=BOTH)
    frame_three = FrameThree(root)
    frame_three.pack(side=LEFT, expand=YES, fill=BOTH)
    frame_two = FrameTwo(root)
    frame_two.pack(side=LEFT, expand=YES, fill=BOTH)
    frame_one.screen_refresh(player1.stats)
    frame_two.screen_refresh(player2.stats)






# add_frames(root)
root.mainloop()