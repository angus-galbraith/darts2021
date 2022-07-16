from tkinter import *



# set main menu
root = Tk()
root.title('Darts')
#root.iconbitmap()
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)

#menu commnds
def darts_new_game():
    hide_all_frames()
    fiveohone_newgame_frame.pack(fill='both', expand=1)

def rtb_new_game():
    hide_all_frames()
    rtb_newgame_frame.pack(fill='both', expand=1)

def hide_all_frames():
    fiveohone_newgame_frame.pack_forget()
    rtb_newgame_frame.pack_forget()

def fiveohone_start():
    hide_all_frames()
    fiveohone_game_frame.pack(fill='both', expand=1)
    
    



# setup menu 
fiveohone_menu = Menu(my_menu)
my_menu.add_cascade(label='501', menu=fiveohone_menu)
fiveohone_menu.add_command(label='New Game', command=darts_new_game)

rtb_menu = Menu(my_menu)
my_menu.add_cascade(label='Roundthe Board', menu=rtb_menu)
rtb_menu.add_command(label='New Game', command=rtb_new_game)



#setup frames(
fiveohone_newgame_frame = Frame(root, width=400, height=400, bg='blue')
fiveohone_game_frame = Frame(root, width=400, height=400, bg='yellow')
rtb_newgame_frame = Frame(root, width=400, height=400, bg='red')

#populate frames

# 501 newgame
fiveohone_name_label = Label(fiveohone_newgame_frame, text='Player Name')
fiveohone_name_label.grid(row=0, column=0)
fiveohone_start_button = Button(fiveohone_newgame_frame, text='Start', command=fiveohone_start)
fiveohone_start_button.grid(row=0, column=1)
root.mainloop()