from tkinter import*
from tkinter.ttk import  Style, Label, Combobox


class MainApplication(Frame):



    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        #Frame.__init__(self, self.master)
        self.configure_gui()
        #self.create_widgets()



    def configure_gui(self):
        self.master.title("Darts")
        
        root.geometry('{}x{}'.format(850, 650))
        

        #create  and layout Main frame
        top_frame = Frame(root, width=800, height=500,pady=3)
        top_frame.grid(row=0, sticky="ew")


        #create inside frames
        frame1 = Frame(top_frame, width=200, height=450)
        frame2 = Frame(top_frame, width=200, height=450, border=2, relief=RAISED)
        frame3 = Frame(top_frame, width=200, height=450, border=2, relief=RAISED)
        frame4 = Frame(top_frame, width=200, height=450, border=2, relief=RAISED)
        frame2top = Frame(frame2, width=200, height=200)
        frame2bottom = Frame(frame2, width=200, height=200)


        #layout inside frames
        frame1.grid(row=0, sticky='ew')
        frame2.grid(row=0, column=1, sticky='ew')
        frame2top.grid(row=0, column=0, sticky='nsew')
        frame2bottom.grid(row=1, column=0, sticky='nsew')
        frame3.grid(row=0, column=2, sticky='ew')
        frame4.grid(row=0, column=3, sticky='ew')

        #frame1 labels
        Label(frame1, text="Player:").grid(row=0, column=0, sticky='w')
        Label(frame1, text="Angus").grid(row=0, column=1, sticky='e')
        Label(frame1, text="Sets:").grid(row=1, column=0, sticky='w')

        #frame2 labels

        #top
        self.remlabel = Label(frame2top, text="Remaining")
        self.remlabel.grid(row=0, column=0, columnspan=2, sticky='e')
        self.remlabel.configure(font=(None, 15))
        self.remlabel1 = Label(frame2top, text="501")
        self.remlabel1.grid(row=1, column=0, sticky='w')
        self.remlabel1.configure(font=(None, 25))

        #bottom
        self.remlabel2 = Label(frame2bottom, text="Remaining")
        self.remlabel2.grid(row=0, column=0, columnspan=2, sticky='e')
        self.remlabel2.configure(font=(None, 15))

        


        #frame4 labels
        Label(frame4, text="Player:").grid(row=0, column=0, sticky='w')








if __name__=='__main__':
    root = Tk()
    main_app = MainApplication(root)

    root.mainloop()
    
