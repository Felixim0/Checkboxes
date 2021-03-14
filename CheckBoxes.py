from tkinter import *
master = Tk()

def clear():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)

def var_states():
    runningTotal = 0
    crucial=0
    totalShifts=0
    #print("Shift1: %d,\nShift2: %d, \nShift3: %d, \nShift4: %d,\nShift5: %d, \nShift6: %d" % (var1.get(), var2.get(),var3.get(),var4.get(), var5.get(),var6.get()))
    if (var1.get()) == 1:
        runningTotal = runningTotal+350
        totalShifts=totalShifts+1
        
    if (var2.get()) == 1:
        runningTotal = runningTotal+500
        crucial=crucial+1
        totalShifts=totalShifts+1
        
    if (var3.get()) == 1:
        runningTotal = runningTotal+350
        totalShifts=totalShifts+1
        
    if (var4.get()) == 1:
        runningTotal = runningTotal+350
        totalShifts=totalShifts+1

    if (var5.get()) == 1:
        runningTotal = runningTotal+500
        crucial=crucial+1
        totalShifts=totalShifts+1

    if (var6.get()) == 1:
        runningTotal = runningTotal+500
        crucial=crucial+1
        totalShifts=totalShifts+1

    if crucial>1:
        runningTotal=runningTotal+350

    if totalShifts>3:
        print ("Invalid - You can only have a maximum of 3 shifts")
        runningTotal=0
        crucial=0
        clear()

    if runningTotal>0:
        print ("Your total extra moneys earnt is " + str(runningTotal) + ".")

    if totalShifts==3:
        print ("You also get a £50 Cinema trip deal")
        
    if crucial>0:
        print ("You also get a £100 family meal deal")
        
    print ("\n")

def genericCommand():
    #print("You have done something to a button")
    buttonStates=[0,0,0,0,0,0]
    if (var1.get()) == 1:
        buttonStates[0]=1
    else:
        buttonStates[0]=0
    if (var2.get()) == 1:
        buttonStates[1]=1
    else:
        buttonStates[1]=0
        
    if (var3.get()) == 1:
        buttonStates[2]=1
    else:
        buttonStates[2]=0
        
    if (var4.get()) == 1:
        buttonStates[3]=1
    else:
        buttonStates[3]=0

    if (var5.get()) == 1:
        buttonStates[4]=1
    else:
        buttonStates[4]=0

    if (var6.get()) == 1:
        buttonStates[5]=1
    else:
        buttonStates[5]=0
    print(buttonStates)

    numberActiveButtons=(buttonStates.count(1))
    if numberActiveButtons > 2:
        #print("You have the maximum number of shifts selected")
        #Add code to disable all buttons with the value of zero in the arrat buttonStates!!!
        if buttonStates[0]==1:
            button1.config(state=NORMAL)
        else:
            button1.config(state=DISABLED)

        if buttonStates[1]==1:
            button2.config(state=NORMAL)
        else:
            button2.config(state=DISABLED)

        if buttonStates[2]==1:
            button3.config(state=NORMAL)
        else:
            button3.config(state=DISABLED)

        if buttonStates[3]==1:
            button4.config(state=NORMAL)
        else:
            button4.config(state=DISABLED)

        if buttonStates[4]==1:
            button5.config(state=NORMAL)
        else:
            button5.config(state=DISABLED)

        if buttonStates[5]==1:
            button6.config(state=NORMAL)
        else:
            button6.config(state=DISABLED)
    else:
        button1.config(state=NORMAL)
        button2.config(state=NORMAL)
        button3.config(state=NORMAL)
        button4.config(state=NORMAL)
        button5.config(state=NORMAL)
        button6.config(state=NORMAL)
               

Label(master, text="Your Extra Shifts:").grid(row=0, sticky=W)
var1 = IntVar()
button1 = Checkbutton(master, text="Christmas Eve until midnight", variable=var1, command=genericCommand)
button1.grid(row=1, sticky=W)
var2 = IntVar()
button2 =Checkbutton(master, text="Christmas Day 00:00 till midday - crucial shift", variable=var2, command=genericCommand)
button2.grid(row=2, sticky=W)
var3 = IntVar()
button3 =Checkbutton(master, text="Christmas Day 12 Noon till midnight", variable=var3, command=genericCommand)
button3.grid(row=3, sticky=W)
var4 = IntVar()
button4 =Checkbutton(master, text="Boxing Day 00:00 till midday", variable=var4, command=genericCommand)
button4.grid(row=4, sticky=W)
var5 = IntVar()
button5 =Checkbutton(master, text="New Years Eve until midnight - Crucial shift", variable=var5, command=genericCommand)
button5.grid(row=5, sticky=W)
var6 = IntVar()
button6 =Checkbutton(master, text="New Years Day 00:00 till midday - Crucial shift", variable=var6, command=genericCommand)
button6.grid(row=6, sticky=W)

Button(master, text='Clear', command=clear).grid(row=7, sticky=W, pady=4)#make it excecute the Generic Command!
Button(master, text='Done', command=var_states).grid(row=8, sticky=W, pady=4)
master.wm_title("Shift Calculator")
mainloop()
