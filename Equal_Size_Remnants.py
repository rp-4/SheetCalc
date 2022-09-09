from tkinter import *
from tkinter import ttk
from tkinter import messagebox



def result():
    size = sheet.get()
    if size.isdigit():
        size = float(sheet.get())
    else:
        messagebox.showerror('Wait What?','Please enter number.')
        return
    
    length = float(mainText_entry.get())
    result = (size - (length/2))
    result = format(result,'.4f')
    finalResult_label.config(text=result)

    
# defining window
root = Tk()
root.title("Equal Size Remnants Calc V0.1")
sq = 240
root.geometry(f'{sq}x{sq}')
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
mainText_entry = ttk.Entry(mainframe, width=18, textvariable=mainText)
mainText_entry.grid(row=3, column=0, columnspan=2, pady=10)



# Add, delete, update and copy buttons
ttk.Button(mainframe, text = "Result",command = result).grid(row=4, column=0, columnspan=2, pady=5)


madeBy = Label(root, text="Developed by r Patel with 💙 !!")
madeBy.grid(row=5, column=0, columnspan=4, pady=5)
root.mainloop()
