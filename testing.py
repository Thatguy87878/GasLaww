# Startup and setting the window up

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Gas Law")
window.configure(bg="white")
# 430 x 290 (standard size)
height_window = 530
width_window = 290

# Declaring some var 

mole_answer = ''
pressure_answer = ''
temp_answer = ''
volume_answer = ''

boyle = IntVar()
charle = IntVar()
avogadro = IntVar()
lussac = IntVar() 
combined = IntVar()

answer = IntVar()

pressure_1 = IntVar()
temp_1 = IntVar()
volume_1 = IntVar()
moles_1 = IntVar()

# Checkbox Set

check1 = Checkbutton(window, variable=boyle, bg='white', text="Boyle's", onvalue=1, offvalue=0)
check2 = Checkbutton(window, variable=charle, bg='white', text="Charle's", onvalue=1, offvalue=0)
check3 = Checkbutton(window, variable=avogadro, bg='white', text="Avogadro's", onvalue=1, offvalue=0)
check4 = Checkbutton(window, variable=lussac, bg='white', text="Lussac's", onvalue=1, offvalue=0)
check5 = Checkbutton(window, variable=combined, bg='white', text="Combined", onvalue=1, offvalue=0)

check1.place(x=320, y=30)
check2.place(x=320, y=50)
check3.place(x=320, y=70)
check4.place(x=320, y=90)
check5.place(x=320, y=110)

# Locking the window up

window.maxsize(height_window, width_window)
window.minsize(height_window, width_window)

# Popup Setup

#def popupmsg():
#    popup = Toplevel(window)
#    popup.minsize(150, 150)
#    popup.maxsize(150, 150)
#   popup.title("Error!!!")
#    popup.configure(bg='white')
#    popup_message = Label(popup, text='Error', bg='white')
#    popup_message.place(x=60, y=50)
#    popup_button = Button(popup, text='exit', bg='white', width=10, command=popup.destroy() )
#   popup_button.place(x=35, y=75)

# Input Set 1

pressure = Entry(window, bd=3, textvariable = pressure_1 )
pressure.place(x=10, y=30, width=100, height=30)
pressureT = Label(window, text="Pressure", bg="white", fg="black")
pressureT.place(x=30, y=60, width=53, height=20)

preUnit = Entry(window, bd=3)
preUnit.place(x=110, y=30, width=40, height=30)

temp = Entry(window, bd=3, textvariable = temp_1 )
temp.place(x=10, y=80, width=100, height=30)
tempT = Label(window, text="Temp", bg="white", fg="black")
tempT.place(x=40, y=110, width=33, height=20)

tempUnit = Entry(window, bd=3)
tempUnit.place(x=110, y=80, width=40, height=30)

volume = Entry(window, bd=3, textvariable = volume_1 )
volume.place(x=10, y=130, width=100, height=30)
volumeT = Label(window, text="Volume", bg="white", fg="black")
volumeT.place(x=38, y=160, width=45, height=20)

volUnit = Entry(window, bd=3)
volUnit.place(x=110, y=130, width=40, height=30)

moles = Entry(window, bd=3)
moles.place(x=10, y=180, width=100, height=30, textvariable = moles_1 )
molesT = Label(window, text="Moles", bg="white", fg="black")
molesT.place(x=38, y=210, width=45, height=20)

molUnit = Entry(window, bd=3)
molUnit.place(x=110, y=180, width=40, height=30)


# Input Set 2

pressure2 = Entry(window, bd=3)
pressure2.place(x=180, y=30, width=100, height=30)
pressureT2 = Label(window, text="Pressure", bg="white", fg="black")
pressureT2.place(x=220, y=60, width=53, height=20)

preUnit2 = Entry(window, bd=3)
preUnit2.place(x=280, y=30, width=40, height=30)

temp2 = Entry(window, bd=3)
temp2.place(x=180, y=80, width=100, height=30)
tempT2 = Label(window, text="Temp", bg="white", fg="black")
tempT2.place(x=220, y=110, width=33, height=20)

tempUnit2 = Entry(window, bd=3)
tempUnit2.place(x=280, y=80, width=40, height=30)

volume2 = Entry(window, bd=3)
volume2.place(x=180, y=130, width=100, height=30)
volumeT2 = Label(window, text="Volume", bg="white", fg="black")
volumeT2.place(x=220, y=160, width=45, height=20)

volUnit2 = Entry(window, bd=3)
volUnit2.place(x=280, y=130, width=40, height=30)

moles2 = Entry(window, bd=3)
moles2.place(x=180, y=180, width=100, height=30)
molesT2 = Label(window, text="Moles", bg="white", fg="black")
molesT2.place(x=220, y=210, width=45, height=20)

molUnit2 = Entry(window, bd=3)
molUnit2.place(x=280, y=180, width=40, height=30)

# Output Set

pressure3 = Label(window, highlightthickness=3, text=pressure_answer)
pressure3.config(highlightcolor="gray", highlightbackground="gray")
pressure3.place(x=420, y=30, width=100, height=30)
pressureT3 = Label(window, text="Pressure", bg="white", fg="black")
pressureT3.place(x=444, y=60, width=53, height=20)

temp3 = Label(window, highlightthickness=3, text=temp_answer)
temp3.config(highlightcolor="gray", highlightbackground="gray")
temp3.place(x=420, y=80, width=100, height=30)
tempT3 = Label(window, text="Temp", bg="white", fg="black")
tempT3.place(x=450, y=110, width=33, height=20)

volume3 = Label(window, highlightthickness=3, text=volume_answer)
volume3.config(highlightcolor="gray", highlightbackground="gray")
volume3.place(x=420, y=130, width=100, height=30)
volumeT3 = Label(window, text="Volume", bg="white", fg="black")
volumeT3.place(x=448, y=160, width=45, height=20)

moles3 = Label(window, highlightthickness=3, text=mole_answer)
moles3.config(highlightcolor="gray", highlightbackground="gray")
moles3.place(x=420, y=180, width=100, height=30)
molesT3 = Label(window, text="Moles", bg="white", fg="black")
molesT3.place(x=448, y=210, width=45, height=20)

# Clear Button

def clear():
    pressure2.delete(0, END)
    temp2.delete(0, END)
    volume2.delete(0, END)
    moles2.delete(0, END)

    pressure.delete(0, END)
    temp.delete(0, END)
    volume.delete(0, END)
    moles.delete(0, END)

    check5.deselect()
    check4.deselect()
    check3.deselect()
    check2.deselect()
    check1.deselect()

clearB = Button(window, command=clear, text='Clear')
clearB.config(width=25, height=20, bg='black', fg='white', bd=5)
clearB.place(x=250, y=250, width=80, height=25)

# Submit Button 



def submit():
    # Convert mL to L 

    if (str(volUnit) == 'mL' ):
        ( volume_1 / 1000 ) = converted
    if (boyle.get() == 1 and charle.get() == 1) or (boyle.get() == 1 and avogadro.get() == 1) or (boyle.get() == 1 and lussac.get() == 1) or (boyle.get() == 1 and combined.get() == 1) or (charle.get() == 1 and avogadro.get() == 1) or (charle.get() == 1 and lussac.get() == 1) or (charle.get() == 1 and combined.get() == 1) or (avogadro.get() == 1 and lussac.get() == 1) or (avogadro.get() == 1 and combined.get() == 1) or (lussac.get() == 1 and combined.get() == 1):
        messagebox.showerror('Error!!!', 'Too many laws selected!')
    elif (boyle.get() ==1 ):
        if (str(preUnit.get())== 'atm' ) and (str(preUnit2.get() == 'atm')):
            print('bitch')
        #elif ():
            #exit()
        else:
            exit()
    else:
        messagebox.showerror('Error!!!', 'No laws selected!')

submitB = Button(window, command=submit, text='Submit')
submitB.config(width=30, height=20, bg='black', fg='white', bd=5)
submitB.place(x=160, y=250, width=80, height=25)

# Starting the window 

window.mainloop()