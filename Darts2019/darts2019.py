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
        #width = root.winfo_screenwidth()
        #height = root.winfo_screenheight()
        root.geometry("%dx%d" % (1200, 900))
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        
        

        # create frames
        
        top_frame = Frame(self.master,width=1000, height=50)
        
        
        center_frame = Frame(self.master, bg='gray2', width=1000, height=40)
        
        btm_frame = Frame(self.master, bg='pink', width=1000, height=45, pady=3)
        

        

        top_frame.grid(row=0, sticky="ew")
        center_frame.grid(row=1, sticky="nsew")
        
        btm_frame.grid(row=3, sticky="ew")


        # layout top frame
        top_frame.grid_rowconfigure(1, weight=1)
        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_columnconfigure(1, weight=1)

        tp_left = Frame(top_frame, bg='blue', height=50)
        tp_right = Frame(top_frame, bg='white',  height=50)

        tp_left.grid(row=0, column=0, sticky="ew")
        tp_right.grid(row=0, column=1, sticky="ew")


        
        #layout centre frames

        center_frame.grid_rowconfigure(0, weight=1)
        center_frame.grid_columnconfigure(0, weight=1)
        center_frame.grid_columnconfigure(1, weight=1)
        center_frame.grid_columnconfigure(2, weight=1)
        center_frame.grid_columnconfigure(3, weight=1)

        ctr_left = Frame(center_frame, bg='light grey')
        ctr_mid = Frame(center_frame, bg='white')
        ctr_mid2 = Frame(center_frame, bg='white')
        ctr_right = Frame(center_frame, bg='light grey')

        ctr_left.grid(row=0, column=0, sticky="nsew")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_mid2.grid(row=0, column=2, sticky="nsew")
        ctr_right.grid(row=0, column=3, sticky="nsew")

        
        # layout bottom frame
        btm_frame.grid_rowconfigure(1, weight=1)
        btm_frame.grid_columnconfigure(0, weight=1)
        btm_frame.grid_columnconfigure(1, weight=1)

        btm_left = Frame(btm_frame, bg='blue', height=50)
        btm_right = Frame(btm_frame, bg='white',  height=50)

        btm_left.grid(row=0, column=0, sticky="ew")
        btm_right.grid(row=0, column=1, sticky="ew")

        #widgets in top frames

        #widgets in middle frames

        #frame1
        ctr_leftlabel1 = Label(ctr_left, text="Totals",font=(None, 20))
        ctr_leftlabel1.grid(row=0, column=0, sticky='w')
        Label(ctr_left, text="Sets:", font=(None, 20)).grid(row=1, column=0, sticky='w')
        Label(ctr_left, text="Legs:", font=(None, 20)).grid(row=2, column=0, sticky='w')
        Label(ctr_left, text="180:", font=(None, 20)).grid(row=3, column=0, sticky='w')
        Label(ctr_left, text="140+:", font=(None, 20)).grid(row=4, column=0, sticky='w')
        Label(ctr_left, text="100+:", font=(None, 20)).grid(row=5, column=0, sticky='w')
        Label(ctr_left, text="80+:", font=(None, 20)).grid(row=6, column=0, sticky='w')
        Label(ctr_left, text="60+:", font=(None, 20)).grid(row=7, column=0, sticky='w')
        Label(ctr_left, text="", font=(None, 20)).grid(row=8, column=0, sticky='w')
        Label(ctr_left, text="Averages", font=(None, 20)).grid(row=9, column=0, sticky='w')
        Label(ctr_left, text="3 Darts:", font=(None, 20)).grid(row=10, column=0, sticky='w')
        Label(ctr_left, text="Checkout%:", font=(None, 20)).grid(row=11, column=0, sticky='w')
        Label(ctr_left, text="Checkout (hit/thrown):", font=(None, 20)).grid(row=12, column=0, sticky='w')

        #frame2
        ctr_mid.grid_columnconfigure(0, weight=1)
        ctr_mid.grid_columnconfigure(1, weight=1)
        ctr_label1 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label1.grid(row=0, column=0, sticky='ew')
        ctr_label2 = Label(ctr_mid, text="501", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label2.grid(row=0, column=1, sticky='ew')
        ctr_label3 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label3.grid(row=1, column=0, sticky='ew')
        ctr_label4 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label4.grid(row=1, column=1, sticky='ew')
        ctr_label5 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label5.grid(row=2, column=0, sticky='ew')
        ctr_label6 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label6.grid(row=2, column=1, sticky='ew')
        ctr_label7 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label7.grid(row=3, column=0, sticky='ew')
        ctr_label8 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label8.grid(row=3, column=1, sticky='ew')
        ctr_label9 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label9.grid(row=4, column=0, sticky='ew')
        ctr_label10 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label10.grid(row=4, column=1, sticky='ew')
        ctr_label11 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label11.grid(row=5, column=0, sticky='ew')
        ctr_label12 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label12.grid(row=5, column=1, sticky='ew')
        ctr_label13 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label13.grid(row=6, column=0, sticky='ew')
        ctr_label14 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label14.grid(row=6, column=1, sticky='ew')
        ctr_label15 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label15.grid(row=7, column=0, sticky='ew')
        ctr_label16 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label16.grid(row=7, column=1, sticky='ew')
        ctr_label17 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label17.grid(row=8, column=0, sticky='ew')
        ctr_label18 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label18.grid(row=8, column=1, sticky='ew')
        ctr_label19 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label19.grid(row=9, column=0, sticky='ew')
        ctr_label20 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label20.grid(row=9, column=1, sticky='ew')
        ctr_label21 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label21.grid(row=10, column=0, sticky='ew')
        ctr_label22 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label22.grid(row=10, column=1, sticky='ew')
        ctr_label23 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label23.grid(row=11, column=0, sticky='ew')
        ctr_label24 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label24.grid(row=11, column=1, sticky='ew')
        ctr_label25 = Label(ctr_mid, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label25.grid(row=12, column=0, sticky='ew')
        ctr_label26 = Label(ctr_mid, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label26.grid(row=12, column=1, sticky='ew')

        #frame3
        ctr_mid2.grid_columnconfigure(0, weight=1)
        ctr_mid2.grid_columnconfigure(1, weight=1)
        ctr_label1 = Label(ctr_mid2, text="", font=(None, 30), borderwidth=2, relief="groove")
        ctr_label1.grid(row=0, column=0, sticky='ew')
        ctr_label2 = Label(ctr_mid2, text="501", font=(None, 30), borderwidth=2, relief="groove")
        ctr_label2.grid(row=0, column=1, sticky='ew')
        ctr_label3 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label3.grid(row=1, column=0, sticky='ew')
        ctr_label4 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label4.grid(row=1, column=1, sticky='ew')
        ctr_label5 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label5.grid(row=2, column=0, sticky='ew')
        ctr_label6 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label6.grid(row=2, column=1, sticky='ew')
        ctr_label7 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label7.grid(row=3, column=0, sticky='ew')
        ctr_label8 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label8.grid(row=3, column=1, sticky='ew')
        ctr_label9 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label9.grid(row=4, column=0, sticky='ew')
        ctr_label10 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label10.grid(row=4, column=1, sticky='ew')
        ctr_label11 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label11.grid(row=5, column=0, sticky='ew')
        ctr_label12 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label12.grid(row=5, column=1, sticky='ew')
        ctr_label13 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label13.grid(row=6, column=0, sticky='ew')
        ctr_label14 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label14.grid(row=6, column=1, sticky='ew')
        ctr_label15 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label15.grid(row=7, column=0, sticky='ew')
        ctr_label16 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label16.grid(row=7, column=1, sticky='ew')
        ctr_label17 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label17.grid(row=8, column=0, sticky='ew')
        ctr_label18 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label18.grid(row=8, column=1, sticky='ew')
        ctr_label19 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label19.grid(row=9, column=0, sticky='ew')
        ctr_label20 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label20.grid(row=9, column=1, sticky='ew')
        ctr_label21 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label21.grid(row=10, column=0, sticky='ew')
        ctr_label22 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label22.grid(row=10, column=1, sticky='ew')
        ctr_label23 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label23.grid(row=11, column=0, sticky='ew')
        ctr_label24 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label24.grid(row=11, column=1, sticky='ew')
        ctr_label25 = Label(ctr_mid2, text="", anchor='center', font=(None, 30), borderwidth=2, relief="groove")
        ctr_label25.grid(row=12, column=0, sticky='ew')
        ctr_label26 = Label(ctr_mid2, text="", anchor='center',font=(None, 30), borderwidth=2, relief="groove")
        ctr_label26.grid(row=12, column=1, sticky='ew')

        #frame4
        ctr_righlabel1 = Label(ctr_right, text="Totals",font=(None, 20))
        ctr_righlabel1.grid(row=0, column=0, sticky='w')
        Label(ctr_right, text="Sets:", font=(None, 20)).grid(row=1, column=0, sticky='w')
        Label(ctr_right, text="Legs:", font=(None, 20)).grid(row=2, column=0, sticky='w')
        Label(ctr_right, text="180:", font=(None, 20)).grid(row=3, column=0, sticky='w')
        Label(ctr_right, text="140+:", font=(None, 20)).grid(row=4, column=0, sticky='w')
        Label(ctr_right, text="100+:", font=(None, 20)).grid(row=5, column=0, sticky='w')
        Label(ctr_right, text="80+:", font=(None, 20)).grid(row=6, column=0, sticky='w')
        Label(ctr_right, text="60+:", font=(None, 20)).grid(row=7, column=0, sticky='w')
        Label(ctr_right, text="", font=(None, 20)).grid(row=8, column=0, sticky='w')
        Label(ctr_right, text="Averages", font=(None, 20)).grid(row=9, column=0, sticky='w')
        Label(ctr_right, text="3 Darts:", font=(None, 20)).grid(row=10, column=0, sticky='w')
        Label(ctr_right, text="Checkout%:", font=(None, 20)).grid(row=11, column=0, sticky='w')
        Label(ctr_right, text="Checkout (hit/thrown):", font=(None, 20)).grid(row=12, column=0, sticky='w')



        #widgets in bottom frames





if __name__=='__main__':
    root = Tk()
    main_app = MainApplication(root)

    root.mainloop()
    
