from tkinter import *

operator = ""


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClearDisplay():
    global operator
    label_request.config(text="")
    operator = ""
    text_input.set("")


def btnEqualsInput():
    try:
        global operator
        label_request.config(text=f"{operator}")
        sumup = str(eval(operator))
        text_input.set(sumup)
        operator = ""
    except:
        text_input.set("invalid value")


if __name__ == "__main__":
    win = Tk()
    win.geometry("310x480")
    win.resizable(width=False, height=False)
    win.title("Calculator")
    color = "#092033"
    color2 = "#0a2d45"
    num_color = "#27e6cf"
    win.configure(bg=color)

    Label(win, text="Calculator", fg="white", background=color,
          font=("arial", 10, "bold")).pack()

    # =================Frame1=========================================
    frame1 = Frame(win, background=color, width="320", height="50",
                   )
    frame1.pack()  # -->> for None

    frame2 = Frame(win, background=color, width="320", height="40",
                   )
    frame2.pack()  # for lable reqests

    frame3 = Frame(win, background=color, width="320", height="60",
                   )
    frame3.pack(pady=1.5)  # for Entry

    frame4 = Frame(win, background=color2, width="320", height="70")
    frame4.pack()  # for line 7 8 9 +

    frame5 = Frame(win, background=color2, width="320", height="70")
    frame5.pack()  # for 4 5 6 -

    frame6 = Frame(win, background=color2, width="320", height="70")

    frame6.pack()  # for 1 2 3 *

    frame7 = Frame(win, background=color2, width="320", height="70")
    frame7.pack()  # for 0 c = /
    # =====================Display=======================

    label_request = Label(frame2, text="", fg="white", background=color,
                          font=("arial", 10, "bold"))
    label_request.pack(side=LEFT)

    text_input = StringVar()
    txtDisplay = Entry(
        frame3,
        font=('arial', 20, 'bold'),
        textvariable=text_input,
        bd=0,
        fg="white",
        insertwidth=4, bg='#092033', justify='right')
    txtDisplay.pack(pady=10)
    # ==================Button========================================

    Button(frame4, padx=23, pady=16, bd=0, fg="white", bg=color2,
           font=('arial', 20),
           text='7', command=lambda: btnClick(7)).grid(row=1, column=0)
    Button(frame4, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='8', command=lambda: btnClick(8)).grid(row=1, column=1)
    Button(frame4, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='9', command=lambda: btnClick(9)).grid(row=1, column=2)
    Button(frame4, padx=23, pady=16, bd=0, fg=num_color, bg=color2,
           font=('arial', 20),
           text='+', command=lambda: btnClick('+')).grid(row=1, column=3)
    # ======================================================================================
    Button(frame5, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='4', command=lambda: btnClick(4)).grid(row=2, column=0)
    Button(frame5, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='5', command=lambda: btnClick(5)).grid(row=2, column=1)
    Button(frame5, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='6', command=lambda: btnClick(6)).grid(row=2, column=2)
    Button(frame5, padx=23, pady=16, bd=0, fg=num_color, bg=color2,
           font=('arial', 20),
           text='-', command=lambda: btnClick('-')).grid(row=2, column=3)
    # ======================================================================================
    Button(frame6, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='1', command=lambda: btnClick(1)).grid(row=3, column=0)
    Button(frame6, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='2', command=lambda: btnClick(2)).grid(row=3, column=1)
    Button(frame6, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='3', command=lambda: btnClick(3)).grid(row=3, column=2)
    Button(frame6, padx=23, pady=16, bd=0, fg=num_color, bg=color2,
           font=('arial', 20),
           text='*', command=lambda: btnClick('*')).grid(row=3, column=3)
    # ======================================================================================
    Button(frame7, padx=23, pady=16, bd=0, fg='white', bg=color2,
           font=('arial', 20),
           text='0', command=lambda: btnClick(0)).grid(row=4, column=0)
    Button(frame7, padx=23, pady=20, bd=0, fg='#df1a32', bg=color2,
           font=('arial', 18),
           text='C', command=btnClearDisplay).grid(row=4, column=1)
    Button(frame7, padx=23, pady=16, bd=0, fg=num_color, bg=color2,
           font=('arial', 20),
           text='=', command=btnEqualsInput).grid(row=4, column=2)
    Button(frame7, padx=25, pady=16, bd=0, fg=num_color, bg=color2,
           font=('arial', 20),
           text='/', command=lambda: btnClick('/')).grid(row=4, column=3)

    win.mainloop()
