from tkinter import *
import datetime


def show_frame(frame):
    frame.tkraise()


def room_selected_command(event):
    pass
    # print(roomSelected.get())


def updateTime():
    now = datetime.datetime.now()
    timeLabel.config(text=now.strftime("%Y-%m-%d %H:%M:%S"))
    timeLabel.after(1000, updateTime)


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
now = datetime.datetime.now()
timeLabel = Label(menu_Frame,
                  text=now.strftime("%Y-%m-%d %H:%M:%S"),
                  font="ariel 20",
                  pady=20,
                  width=20,
                  border=5,)
timeLabel.place(x=950, y=650)
timeLabel.after(1000, updateTime)

# ======================= 1.Check in Frame Code ================
checkinLabel = Label(checkin_Frame,
                     text="CHECK IN",
                     font="Times 20",
                     pady=20,
                     width=20,
                     border=5
                     ).pack(padx=10, pady=10)

nameLabel = Label(checkin_Frame,
                  text="Enter name :",
                  font="Times 20",
                  width=20,
                  border=5
                  ).place(x=20, y=100)

nameEntry = Entry(checkin_Frame,
                  font="Times 20",
                  width=40,
                  border=5
                  ).place(x=400, y=100)

roomLabel = Label(checkin_Frame,
                  text="Enter room type :",
                  font="Times 20",
                  width=20,
                  border=5
                  ).place(x=20, y=200)

roomType = ["Normal", "Deluxe", "Floor"]
roomSelected = StringVar()
roomSelected.set(roomType[0])
roomOptions = OptionMenu(checkin_Frame, roomSelected,
                         *roomType, command=room_selected_command)
roomOptions.place(x=340, y=200)
roomOptions.config(font="Times 18")

amountDayLabel = Label(checkin_Frame,
                       text="How long ? (days) :",
                       font="Times 20",
                       width=20,
                       border=5
                       ).place(x=500, y=200)

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
daySelected = IntVar()
daySelected.set(days[0])
dayOption = OptionMenu(checkin_Frame, daySelected,
                       *days, command=room_selected_command)
dayOption.place(x=800, y=200)
dayOption.config(font="Times 18")

dateLabel = Label(checkin_Frame,
                  text="Enter date (yy-dd-mm):",
                  font="Times 20",
                  width=20,
                  border=5
                  ).place(x=20, y=300)

dateEntry = Entry(checkin_Frame,
                  font="Times 20",
                  width=30,
                  border=5
                  ).place(x=400, y=300)

phoneLabel = Label(checkin_Frame,
                   text="Enter phone number:",
                   font="Times 20",
                   width=20,
                   border=5
                   ).place(x=20, y=400)

phoneEntry = Entry(checkin_Frame,
                   font="Times 20",
                   width=30,
                   border=5
                   ).place(x=400, y=400)

checkin_submit_btn = Button(checkin_Frame,
                            text="SUBMIT",
                            font="Times 15",
                            pady=20,
                            width=20,
                            border=5
                            ).place(x=500, y=500)

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
