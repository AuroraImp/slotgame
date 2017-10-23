

from Tkinter import *
import Tkinter as tk
import random
import tkMessageBox
""" Setting The Main GUI """
    
w1 = 0
w2 = 0
w3 = 0
cash=1000
bet=0
win=0

def gameplay():
    global cash
    global win
    str_bet=bet.get()
    bbet=int(str_bet)

    if  0>bbet or bbet>cash :
        messagebox.showinfo("Error", "Enter Correct Money")
    else:
        cash=cash-bbet
    
        l1= ('$$$','Pizza','Horse','Fish','Potato','Love')
        w1 = random.choice(l1)
        w2 = random.choice(l1)
        w3 = random.choice(l1)
        print (w1,w2,w3, cash)

        str_in1=in1.get()
        str_in2=in2.get()
        str_in3=in3.get()

        list1 = [str_in1,str_in2,str_in3]
        list2 = [w1,w2,w3]
        s1 = set(list1)&set(list2)


        if str_in1 == w1 and str_in2 == w2 and str_in3 == w3:
            win=(bbet*10)
            cash=win+cash
            
        elif str_in1 == w1 and str_in2 == w2:
            win=(bbet*5)
            cash=win+cash

        elif str_in2 == w2 and str_in3 == w3:
            win=(bbet*5)
            cash=win+cash

        elif str_in1 == w1 and str_in3 == w3:
            win=(bbet*5)
            cash=win+cash

        elif len(s1) == 3:
             win=(bbet*5)
             cash=win+cash
             
        elif len(s1) == 2:
             win=(bbet*2)
             cash=win+cash

        elif len(s1) == 1 or len(s1) == 0:
             win=(bbet*0)
              
             

            

    ii=Label(topframe, text="", font=("Helvetica", 25))
    ii.grid(row = 0, column = 1)
    ii.configure(text="     Cash: %d     " %cash)
        
    jj=Label(topframe, text="", font=("Helvetica", 25))
    jj.grid(row = 0, column = 0)
    jj.configure(text="     Win: %d     " %win)

    
    kk=Label(mainframe, text="", font=("Helvetica", 25))
    kk.grid(row = 2, column = 3)
    kk.configure(text="  %s  " %w1)

    
    ll=Label(mainframe, text="", font=("Helvetica", 25))
    ll.grid(row = 2, column = 4)
    ll.configure(text="  %s  " %w2)

    mm=Label(mainframe, text="", font=("Helvetica", 25))
    mm.grid(row = 2, column = 5)
    mm.configure(text="  %s  " %w3)


GUI= Tk()
GUI.title("Gambling")
bgf=Frame(GUI)
bgf=Frame(GUI,width=400,height=450)

bgf.place(height=7000, width=4000, x=100, y=100)
bgf.config()


bgf.grid_rowconfigure(0,weight=1)
bgf.grid_columnconfigure(0,weight=1)


photo=PhotoImage(file="sgame.gif")
label = Label(GUI,image = photo)
label.image = photo 
label.grid(row=0,column=0,columnspan=20,rowspan=20)



topframe = Frame(GUI)
topframe.grid(column=1,row=1, sticky=(N,W,E,S) )
topframe.rowconfigure(0, weight = 1)
topframe.columnconfigure(0, weight = 1)

ii=Label(topframe, text="     Cash: 1000     ", font=("Helvetica", 25))
ii.grid(row = 0, column = 1)

##icash = StringVar(GUI)
##icash.set(cash)
#input5=StringVar()
#ii=Entry(topframe, text=icash, font=("Helvetica", 6))
#ii.grid(row = 0, column = 1)


mainframe = Frame(GUI)

mainframe.grid(column=1,row=5, sticky=(N,W,E,S) )
mainframe.rowconfigure(0, weight = 1)
mainframe.columnconfigure(0, weight = 1)


c1var = StringVar(GUI)
choices1 = { '$$$','Pizza','Horse','Fish','Potato','Love'}
c1var.set('Love')
input1=StringVar()
in1=Entry(mainframe, text=c1var, font=("Helvetica", 6))
in1.grid_remove

c2var = StringVar(GUI)
choices2 = { '$$$','Pizza','Horse','Fish','Potato','Love'}
c2var.set('$$$')
input2=StringVar()
in2=Entry(mainframe, text=c2var, font=("Helvetica", 6))
in2.grid_remove

c3var = StringVar(GUI)
choices3 = { '$$$','Pizza','Horse','Fish','Potato','Love'}
c3var.set('Fish')
input3=StringVar()
in3=Entry(mainframe, text=c3var, font=("Helvetica", 6))
in3.grid_remove

Label(mainframe, text="Bet: ", font=("Helvetica", 25)).grid(row = 0, column = 6)

yb = StringVar(GUI)
yb.set("50")
input4=StringVar()
bet=Entry(mainframe, text=yb, font=("Helvetica", 20))
bet.grid(row = 0, column = 7)

 
popupMenu1 = OptionMenu(mainframe, c1var, *choices1)
popupMenu1.config(bg="red", font=("Helvetica", 20)) 
popupMenu2 = OptionMenu(mainframe, c2var, *choices2)
popupMenu2.config(bg="red",font=("Helvetica", 20)) 
popupMenu3 = OptionMenu(mainframe, c3var, *choices3)
popupMenu3.config(bg="red",font=("Helvetica", 20)) 

###Label(mainframe, text="              ", font=("Helvetica", 23)).grid(row = 0, column = 1)

popupMenu1.grid(row = 0, column =3)
popupMenu2.grid(row = 0, column =4)
popupMenu3.grid(row = 0, column =5)
 
def change_dropdown(*args):
    c1var.get()
    c2var.get()
    c3var.get()

 
c1var.trace('w', change_dropdown)
c2var.trace('w', change_dropdown)
c3var.trace('w', change_dropdown)


buttonframe = Frame(GUI)

buttonframe.grid(column=6,row=5, sticky=(N,W,E,S) )
buttonframe.rowconfigure(0, weight = 1)
buttonframe.columnconfigure(0, weight = 1)


b = Button(buttonframe, text="Spin Bro!!", bg="red",font=("Helvetica", 25), command=gameplay).pack()
ii = Label(GUI, text=cash)
jj = Label(GUI, text=win)
kk = Label(GUI, text=w1)
ll = Label(GUI, text=w2)
mm = Label(GUI, text=w3)


GUI.mainloop()
