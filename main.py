from tkinter import *
from tkcalendar import *
from tkinter import messagebox
import datetime
import checkin
from tkinter import ttk
import json



def show_frame(frame):
    frame.tkraise()
        
# ref. https://stackabuse.com/insertion-sort-in-python/
def insertion_sort(array,key):
    global data_key
    key_index=data_key.index(key)
    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and array[currentPosition - 1][key_index] > currentValue[key_index]:
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        array[currentPosition] = currentValue
    return array
# ref https://www.delftstack.com/howto/python/sort-list-alphabetically/
def quick_sort(lst,key):
    global data_key
    key_index=data_key.index(key)
    if not lst:
        return []
    return (quick_sort([x for x in lst[1:] if x[key_index] <  lst[0][key_index]],key)
            + [lst[0]] +
            quick_sort([x for x in lst[1:] if x[key_index] >= lst[0][key_index]],key))

def sort_by_userid():
    global data_ls,table,root
    sorted_dat = insertion_sort(data_ls,'user_id')
    for i in table.get_children():
            table.delete(i)
    root.update()
    row = 0
    for ele in sorted_dat:
        table.insert(parent="", 
                    index=row, 
                    values=ele)
        row+=1

def sort_by_name():
    global data_ls,table,root
    sorted_dat = quick_sort(data_ls,'name')
    for i in table.get_children():
            table.delete(i)
    root.update()
    row = 0
    for ele in sorted_dat:
        table.insert(parent="", 
                    index=row, 
                    values=ele)
        row+=1

def sort_by_roomNo():
    global data_ls,table,root
    sorted_dat = quick_sort(data_ls,'room_number')
    for i in table.get_children():
            table.delete(i)
    root.update()
    row = 0
    for ele in sorted_dat:
        table.insert(parent="", 
                    index=row, 
                    values=ele)
        row+=1

def sort_by_surname():
    global data_ls,table,root
    sorted_dat = quick_sort(data_ls,'surname')
    for i in table.get_children():
            table.delete(i)
    root.update()
    row = 0
    for ele in sorted_dat:
        table.insert(parent="", 
                    index=row, 
                    values=ele)
        row+=1


def room_id_selected_command():

    handleError, roomAvarible = checkin.findAvailableRoom(roomTypeSelected.get(
    ), dateCheckin.get_date(), dateCheckout.get_date())

    if handleError != "":
        messagebox.showinfo("Status", handleError)
    else:
        top = Toplevel(root)
        top.geometry("300x300")
        roomOptionsA = OptionMenu(top, roomSelectedVariable, *roomAvarible)
        roomOptionsA.pack()

        closeBtn = Button(top, text="close", command=top.destroy).pack(pady=30)


def handleSubmitData():
    handleError = checkin.writeData(nameEntry.get(), sureNameEntry.get(), phoneEntry.get(
    ), roomTypeSelected.get(), roomSelectedVariable.get(), dateCheckin.get_date(), dateCheckout.get_date())

    messagebox.showinfo("Status", handleError)


def clear_input_command():
    nameEntry.delete(0, 'end')
    sureNameEntry.delete(0, 'end')
    phoneEntry.delete(0, 'end')
    roomTypeSelected.set("Normal")
    roomSelectedVariable.set("\"Not selected\"")
    dateCheckin.set_date(datetime.date.today())
    dateCheckout.set_date(datetime.date.today())


def updateTime():
    now = datetime.datetime.now()
    timeLabel.config(text=now.strftime("%Y-%m-%d %H:%M:%S"))
    timeLabel.after(1000, updateTime)

def read_Json(filename):
    with open(filename) as file:
        data = json.load(file)
    return data


if __name__ == '__main__':

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
    menu_Frame.grid(row=0, column=1, sticky='ne')
    checkin_Frame.grid(row=0, column=0, sticky='nsew')
    guestList_Frame.grid(row=0, column=0, sticky='nsew')
    checkout_Frame.grid(row=0, column=0, sticky='nsew')

    # ======================= Menu Frame code =================
    # welcome_message = Label(menu_Frame,
    #                         text="WELCOME",
    #                         width=600,
    #                         font="Times 56",
    #                         pady=40).pack(padx=10, pady=10)

    checkinBtn = Button(menu_Frame,
                        text="▶CHECK IN",
                        font="Times 15",
                        width=20,
                        background='#8BEEFF',
                        activebackground='#2AD6EC',
                        relief='flat',
                        command=lambda: show_frame(checkin_Frame)
                        ).pack()

    showGuestBtn = Button(menu_Frame,
                          text="👥GUEST LIST",
                          font="Times 15",
                          width=20,
                          background='#8BEEFF',
                          activebackground='#2AD6EC',
                          relief='flat',
                          command=lambda: show_frame(guestList_Frame)
                          ).pack()

    checkOutBtn = Button(menu_Frame,
                         text="◀CHECK OUT",
                         font="Times 15",
                         width=20,
                         background='#8BEEFF',
                         activebackground='#2AD6EC',
                         relief='flat',
                         command=lambda: show_frame(checkout_Frame)
                         ).pack()

    exitBtn = Button(menu_Frame,
                     text="EXIT",
                     font="Times 15",
                     width=20,
                     background='#8BEEFF',
                     activebackground='#2AD6EC',
                     relief='flat',
                     command=quit
                     ).pack()
    now = datetime.datetime.now()
    timeLabel = Label(root,
                      text=now.strftime("%Y-%m-%d %H:%M:%S"),
                      font="ariel 10",
                      pady=20,
                      width=20,
                      border=5,)
    timeLabel.place(x=1100, y=650)
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
                      width=0,
                      border=5
                      ).place(x=50, y=100)

    nameEntry = Entry(checkin_Frame,
                      font="Times 20",
                      width=15,
                      border=5
                      )
    nameEntry.place(x=220, y=100)

    sureNameLabel = Label(checkin_Frame,
                          text="Surename :",
                          font="Times 20",
                          width=20,
                          border=5
                          ).place(x=500, y=100)

    sureNameEntry = Entry(checkin_Frame,
                          font="Times 20",
                          width=15,
                          border=5
                          )
    sureNameEntry.place(x=750, y=100)

    phoneLabel = Label(checkin_Frame,
                       text="Enter phone number:",
                       font="Times 20",
                       width=20,
                       border=5
                       ).place(x=20, y=180)

    phoneEntry = Entry(checkin_Frame,
                       font="Times 20",
                       width=30,
                       border=5
                       )
    phoneEntry.place(x=350, y=180)

    roomLabel = Label(checkin_Frame,
                      text="Enter room type :",
                      font="Times 20",
                      width=0,
                      border=5
                      ).place(x=50, y=260)

    roomType = ["Normal", "Deluxe", "Twin"]
    roomTypeSelected = StringVar()
    roomTypeSelected.set(roomType[0])
    roomOptions = OptionMenu(checkin_Frame, roomTypeSelected,
                             *roomType)
    roomOptions.place(x=340, y=260)
    roomOptions.config(font="Times 18")

    labelDateCheckin = Label(checkin_Frame,
                             text="Date check in :",
                             font="Times 20",
                             width=0,
                             border=5
                             ).place(x=50, y=340)

    dateCheckin = DateEntry(checkin_Frame, selectmode='day',
                            year=now.year, month=now.month, day=now.day)
    dateCheckin.place(x=290, y=350)

    labelDateCheckout = Label(checkin_Frame,
                              text="Date check out :",
                              font="Times 20",
                              width=0,
                              border=5
                              ).place(x=500, y=340)

    dateCheckout = DateEntry(checkin_Frame, selectmode='day',
                             year=now.year, month=now.month, day=now.day)
    dateCheckout.place(x=740, y=350)

    pleaseSelectRoomLabel = Label(checkin_Frame,
                                  text="Select room :",
                                  font="Times 20",
                                  width=0,
                                  border=5
                                  ).place(x=50, y=420)

    roomSelectedVariable = StringVar()
    roomSelectedVariable.set("\"Not selected\"")
    selectedRoomEntry = Entry(checkin_Frame, state=DISABLED,
                              textvariable=roomSelectedVariable,
                              font="Times 20", width=14,
                              border=5
                              ).place(x=220, y=420)

    selectRoomBtn = Button(checkin_Frame, text="Sel Room",
                           font="Times 15", command=room_id_selected_command).place(x=500, y=420)

    clearInputBtn = Button(checkin_Frame, text="Clear input",
                           font="Times 15", command=clear_input_command).place(x=565, y=520)

    checkin_submit_btn = Button(checkin_Frame,
                                text="SUBMIT",
                                font="Times 15",
                                pady=20,
                                width=20,
                                border=5,
                                command=handleSubmitData
                                ).place(x=500, y=600)

    # ======================= 2.SHOW GUEST LIST Frame Code ================
    data = read_Json('Data.json')
    amount_data = list(data.keys())
    data_key = ["user_id",
                "name",
                "surname",
                "tel",
                "room_type",
                "room_number",
                "date_in",
                "date_out"]
    data_ls = []
    for dat in amount_data:
        temp = []
        for ele in data_key:
            temp.append(data.get(dat).get(ele))
        data_ls.append(temp)
    # data_ls = [data.get(n).get('name') for n in data]

    guestListLabel = Label(guestList_Frame,
                        text="GUEST LIST",
                        font="Times 20",
                        pady=20,
                        width=20,
                        border=5
                        ).pack(side='top')

    table_Frame = LabelFrame(guestList_Frame, 
                            text="Data")
    table_Frame.pack(fill=BOTH,expand=YES)


    table_scrollbarx = Scrollbar(table_Frame, 
                                orient='horizontal')
    table_scrollbarx.pack(side=BOTTOM, fill=X)
    # y
    table_scrollbary = Scrollbar(table_Frame, 
                                orient='vertical')
    table_scrollbary.pack(side=RIGHT, fill=Y)

    table = ttk.Treeview(table_Frame, 
                yscrollcommand=table_scrollbary.set, 
                xscrollcommand=table_scrollbarx.set)
    
    table_scrollbary.config(command=table.yview)
    table_scrollbarx.config(command=table.xview)
    table['columns'] = ('User ID', 'Name','Surname','tel','Room Type','Room No.','Date in','Date out')
    table.column("#0",width=0,stretch=True)
    for col in table['columns']:
        table.column(col,anchor=CENTER,width=80)
    
    table.heading("#0",text='',anchor=CENTER)
    for col in table['columns']:
        if col == 'User ID':
            table.heading(col,text=col,anchor=CENTER,command=sort_by_userid)
        elif col == 'Name':
            table.heading(col,text=col,anchor=CENTER,command=sort_by_name)
        elif col == 'Surname':
            table.heading(col,text=col,anchor=CENTER,command=sort_by_surname)
        elif col == 'Room No.':
            table.heading(col,text=col,anchor=CENTER,command=sort_by_roomNo)
        else:
            table.heading(col,text=col,anchor=CENTER)


    table.pack(fill=BOTH,expand=YES)

    # sorted_data_ls = insertion_sort(data_ls,'user_id')
    # print('sorted',sorted_data_ls)
    row = 0
    for ele in data_ls:
        table.insert(parent="", 
                    index=row, 
                    values=ele)
        row+=1
    

    # backBtn = Button(guestList_Frame,
    #                 text="BACK TO MENU",
    #                 font="Times 15",
    #                 pady=20,
    #                 width=20,
    #                 border=5,
    #                 command=lambda: show_frame(menu_Frame)
    #                 ).place(x=10, y=630)

    # ======================= 3.CHECK OUT Frame Code ================
    checkoutLabel = Label(checkout_Frame,
                          text="CHECK OUT",
                          font="Times 20",
                          pady=20,
                          width=20,
                          border=5
                          ).pack(padx=10, pady=10)

    # backBtn = Button(checkout_Frame,
    #                 text="BACK TO MENU",
    #                 font="Times 15",
    #                 pady=20,
    #                 width=20,
    #                 border=5,
    #                 command=lambda: show_frame(menu_Frame)
    #                 ).place(x=10, y=630)

    show_frame(menu_Frame)

    root.mainloop()
