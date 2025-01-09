from time import strftime
from tkinter import Label, Tk
 
window = Tk()
window.title("Digital clock")
window.geometry("200x80")
window.configure(bg="white")  
window.resizable(True, False) 

clock_label = Label(window, bg="white", fg="purple", font=("times", 25, "bold italic"), relief="flat", )
clock_label.place(x=25, y=20)



def update_label():
    """
    This function will update the clock

    every 80 milliseconds
    """
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()

