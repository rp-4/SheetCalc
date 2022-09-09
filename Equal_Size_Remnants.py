from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def numCheck():
    number = list(mainText_entry.get())
    for i in range(0,len(number)):
        if number[i].isdigit() or number[i] == ".":
            #print(number[i])
            return True
        else:
            return False
        

def result():
    if not numCheck():
        messagebox.showerror('Wait What?','Please enter number.')
        clear()
        length = 0
        finalResult_label.config(text="No Number")
        return
    else:
        length = float(mainText_entry.get())
    
    size = float(sheet.get())
    result = (size - (length/2))
    result = format(result,'.4f')
    finalResult_label.config(text=result)

def clear():
    mainText_entry.delete(0,END)
    
# defining window
root = Tk()
root.title("Equal Size Remnants Calc V0.1")
w = 240
h = 250
root.geometry(f'{w}x{h}')
root.resizable(False, False)
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# input boxes

finalResult = StringVar()
finalResult_label = ttk.Label(mainframe, font=('Micross',25), text="Result")
finalResult_label.grid(row=0, column=0, columnspan=2, pady=10)


# Radio buttons for Sheet Size
sheet = StringVar()

size120 = Radiobutton(mainframe, text="120 Inch", font=('Micross',12), variable=sheet, value="120")
size120.grid(row=1, column=0, sticky=W, padx=20)

size985 = Radiobutton(mainframe, text="98.5 Inch", font=('Micross',12), variable=sheet, value="98.5")
size985.grid(row=1, column=1, sticky=W)

size96 = Radiobutton(mainframe, text="96 Inch", font=('Micross',12), variable=sheet, value="96")
size96.grid(row=2, column=0, sticky=W, padx=20)
sheet.set("120")


#Enter length

mainText = StringVar()
mainText_entry = ttk.Entry(mainframe, width=10, font=('Micross',18), textvariable=mainText)
mainText_entry.grid(row=3, column=0, columnspan=2, pady=10)



# Button to get Result
ttk.Button(mainframe, text = "Result", command = result).grid(row=4, column=0, pady=5)

#button to clear
ttk.Button(mainframe, text = "Clear",command = clear).grid(row=4, column=1,  pady=5)

madeBy = Label(root, text="Developed by r Patel with 💙 !!")
madeBy.grid(row=5, column=0, columnspan=4, pady=10)
root.mainloop()
