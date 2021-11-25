from tkinter import *


def show_frame(frame):
    frame.tkraise()


root = Tk()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

width_of_window = 1280
height_of_window = 720
root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window,
              ((root.winfo_screenwidth()/2)-(width_of_window/2)), ((root.winfo_screenheight()/2)-(height_of_window/2))))
root.title("HOTEL MANAGEMENT")
root.resizable(width=False, height=False)

menu_Frame = Frame(root)
checkin_Frame = Frame(root)
guestList_Frame = Frame(root)
checkout_Frame = Frame(root)
menu_Frame.grid(row=0, column=0, sticky='nsew')
checkin_Frame.grid(row=0, column=0, sticky='nsew')
guestList_Frame.grid(row=0, column=0, sticky='nsew')
checkout_Frame.grid(row=0, column=0, sticky='nsew')

# ======================= Menu Frame code =================
welcome_message = Label(menu_Frame,
                        text="WELCOME",
                        width=600,
                        font="Times 56",
                        pady=40).pack(padx=10, pady=10)

checkinBtn = Button(menu_Frame,
                    text="1.CHECK IN",
                    font="Times 20",
                    pady=20,
                    width=20,
                    border=5,
                    command=lambda: show_frame(checkin_Frame)
                    ).pack(padx=10, pady=10)

showGuestBtn = Button(menu_Frame,
                      text="2.SHOW GUEST LIST",
                      font="Times 20",
                      pady=20,
                      width=20,
                      border=5,
                      command=lambda: show_frame(guestList_Frame)
                      ).pack(padx=10, pady=10)

checkOutBtn = Button(menu_Frame,
                     text="3.CHECK OUT",
                     font="Times 20",
                     pady=20,
                     width=20,
                     border=5,
                     command=lambda: show_frame(checkout_Frame)
                     ).pack(padx=10, pady=10)

exitBtn = Button(menu_Frame,
                 text="4.EXIT",
                 font="Times 20",
                 pady=20,
                 width=20,
                 border=5,
                 command=quit
                 ).pack(padx=10, pady=10)

# ======================= 1.Check in Frame Code ================
checkinLabel = Label(checkin_Frame,
                     text="CHECK IN",
                     font="Times 20",
                     pady=20,
                     width=20,
                     border=5
                     ).pack(padx=10, pady=10)

backBtn = Button(checkin_Frame,
                 text="BACK TO MENU",
                 font="Times 15",
                 pady=20,
                 width=20,
                 border=5,
                 command=lambda: show_frame(menu_Frame)
                 ).place(x=10, y=630)

# ======================= 2.SHOW GUEST LIST Frame Code ================
guestListLabel = Label(guestList_Frame,
                       text="GUEST LIST",
                       font="Times 20",
                       pady=20,
                       width=20,
                       border=5
                       ).pack(padx=10, pady=10)

backBtn = Button(guestList_Frame,
                 text="BACK TO MENU",
                 font="Times 15",
                 pady=20,
                 width=20,
                 border=5,
                 command=lambda: show_frame(menu_Frame)
                 ).place(x=10, y=630)

# ======================= 3.CHECK OUT Frame Code ================
checkoutLabel = Label(checkout_Frame,
                      text="CHECK OUT",
                      font="Times 20",
                      pady=20,
                      width=20,
                      border=5
                      ).pack(padx=10, pady=10)

backBtn = Button(checkout_Frame,
                 text="BACK TO MENU",
                 font="Times 15",
                 pady=20,
                 width=20,
                 border=5,
                 command=lambda: show_frame(menu_Frame)
                 ).place(x=10, y=630)


show_frame(menu_Frame)

root.mainloop()
