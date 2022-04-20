# Startup and setting the window up

from tkinter import *
window = Tk()

window.title("Gas Law")
window.configure(bg="white")

height_window = 430
width_window = 290

# Declaring some var 

mole_answer = ''
pressure_answer = ''
temp_answer = ''
volume_answer = ''


# Locking the window up

window.maxsize(height_window, width_window)
window.minsize(height_window, width_window)

# Input Set 1

pressure = Entry(window, bd=3)
pressure.place(x=10, y=30, width=100, height=30)
pressureT = Label(window, text="Pressure", bg="white", fg="black")
pressureT.place(x=30, y=60, width=53, height=20)

temp = Entry(window, bd=3)
temp.place(x=10, y=80, width=100, height=30)
tempT = Label(window, text="Temp", bg="white", fg="black")
tempT.place(x=40, y=110, width=33, height=20)

volume = Entry(window, bd=3)
volume.place(x=10, y=130, width=100, height=30)
volumeT = Label(window, text="Volume", bg="white", fg="black")
volumeT.place(x=38, y=160, width=45, height=20)

moles = Entry(window, bd=3)
moles.place(x=10, y=180, width=100, height=30)
molesT = Label(window, text="Moles", bg="white", fg="black")
molesT.place(x=38, y=210, width=45, height=20)

# Input Set 2

pressure2 = Entry(window, bd=3)
pressure2.place(x=130, y=30, width=100, height=30)
pressureT2 = Label(window, text="Pressure", bg="white", fg="black")
pressureT2.place(x=150, y=60, width=53, height=20)

temp2 = Entry(window, bd=3)
temp2.place(x=130, y=80, width=100, height=30)
tempT2 = Label(window, text="Temp", bg="white", fg="black")
tempT2.place(x=160, y=110, width=33, height=20)

volume2 = Entry(window, bd=3)
volume2.place(x=130, y=130, width=100, height=30)
volumeT2 = Label(window, text="Volume", bg="white", fg="black")
volumeT2.place(x=158, y=160, width=45, height=20)

moles2 = Entry(window, bd=3)
moles2.place(x=130, y=180, width=100, height=30)
molesT2 = Label(window, text="Moles", bg="white", fg="black")
molesT2.place(x=158, y=210, width=45, height=20)

# Output Set

pressure3 = Label(window, highlightthickness=3, text=pressure_answer)
pressure3.config(highlightcolor="gray", highlightbackground="gray")
pressure3.place(x=320, y=30, width=100, height=30)
pressureT3 = Label(window, text="Pressure", bg="white", fg="black")
pressureT3.place(x=340, y=60, width=53, height=20)

temp3 = Label(window, highlightthickness=3, text=temp_answer)
temp3.config(highlightcolor="gray", highlightbackground="gray")
temp3.place(x=320, y=80, width=100, height=30)
tempT3 = Label(window, text="Temp", bg="white", fg="black")
tempT3.place(x=350, y=110, width=33, height=20)

volume3 = Label(window, highlightthickness=3, text=volume_answer)
volume3.config(highlightcolor="gray", highlightbackground="gray")
volume3.place(x=320, y=130, width=100, height=30)
volumeT3 = Label(window, text="Volume", bg="white", fg="black")
volumeT3.place(x=348, y=160, width=45, height=20)

moles3 = Label(window, highlightthickness=3, text=mole_answer)
moles3.config(highlightcolor="gray", highlightbackground="gray")
moles3.place(x=320, y=180, width=100, height=30)
molesT3 = Label(window, text="Moles", bg="white", fg="black")
molesT3.place(x=348, y=210, width=45, height=20)

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

clearB = Button(window, command=clear, text='Clear')
clearB.config(width=25, height=20, bg='black', fg='white', bd=5)
clearB.place(x=300, y=250, width=25, height=20)

# Submit Button 

def submit():
    exit()
    

submitB = Button(window, command=submit, text='Submit')
submitB.config(width=30, height=20, bg='black', fg='black', bd=5)
submitB.place(x=175, y=250, width=80, height=25)






# Starting the window 

window.mainloop()