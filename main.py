from os import name
from tkinter import *
from tkcalendar import *
from tkinter import messagebox
import datetime
import checkin
from tkinter import ttk
import json
from operator import itemgetter
from package import BST
from package import Node


def show_frame(frame):
    frame.tkraise()


def sort_date(lst, key):
    # change yyyy-mm-dd --> yyyymmdd then sort it.
    global data_key
    key_index = data_key.index(key)
    for ele in range(len(lst)-1, 0, -1):
        for it in range(ele):
            if lst[it][key_index].replace("-", "") > lst[it+1][key_index].replace("-", ""):
                temp = lst[it]
                lst[it] = lst[it+1]
                lst[it+1] = temp
    return lst

# ref https://www.delftstack.com/howto/python/sort-list-alphabetically/


def quick_sort(lst, key):
    global data_key
    key_index = data_key.index(key)
    if key == 'Name' or key == 'Surname':
        if not lst:
            return []
        return (quick_sort([x for x in lst[1:] if x[key_index].lower() < lst[0][key_index].lower()], key)
                + [lst[0]] +
                quick_sort([x for x in lst[1:] if x[key_index].lower() >= lst[0][key_index].lower()], key))
    else:
        if not lst:
            return []
        return (quick_sort([x for x in lst[1:] if x[key_index] < lst[0][key_index]], key)
                + [lst[0]] +
                quick_sort([x for x in lst[1:] if x[key_index] >= lst[0][key_index]], key))


def sort_button_command(key):
    global data_ls
    sorted_dat = quick_sort(data_ls, key)
    update_table(data=sorted_dat)


def sortdate_button_command(key):
    global data_ls
    sorted_dat = sort_date(data_ls, key)
    update_table(data=sorted_dat)


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
    global data_ls,id_ls
    id_ls = update_lsbox()
    showID(id_ls)
    handleError = checkin.writeData(nameEntry.get(), sureNameEntry.get(), phoneEntry.get(
    ), roomTypeSelected.get(), roomSelectedVariable.get(), dateCheckin.get_date(), dateCheckout.get_date())
    data_ls = update_data()
    update_table()
    roomSelectedVariable.set("\"Not selected\"")
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


def update_data():
    global data, data_ls, data_key
    data_ls.clear()
    data = read_Json('Data.json')
    for room in data:
        if room != "LastID":
            for items in data[room]["bookingData"]:
                temp = []
                for dat in data_key:
                    temp.append(items.get(dat))
                data_ls.append(temp)
    return data_ls


def deleteData(roomDict):
    data = read_Json("Data.json")
    room = roomDict["name"]
    del roomDict['name']
    date_in = datetime.datetime.strptime(roomDict["dateIn"], "%Y-%m-%d")
    date_out = datetime.datetime.strptime(roomDict["dateOut"], "%Y-%m-%d")

    # del_lst = Date that should delete in bookDate
    del_lst = []
    amountDay = date_out - date_in
    for i in range(amountDay.days):
        baseDt = datetime.datetime.combine(
            date_in, datetime.datetime.min.time())
        dt = baseDt+datetime.timedelta(days=i)
        del_lst.append(str(dt.date()))

    #del data
    for i in del_lst:
        data[room]["dateBooking"].remove(i)
    for i in range(len(data[room]["bookingData"])):
        if data[room]["bookingData"][i]['id'] == roomDict["id"]:
            del data[room]["bookingData"][i]
            print("deleted succcccck!")
            break

    # write
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)


def getRoomByGuestID(guestID):
    # return dict data
    data = read_Json("Data.json")
    for room in data:
        if room != "LastID":
            for items in data[room]["bookingData"]:
                if items["id"] == guestID:
                    items["name"] = f"{room}"
                    return items


def handleSubmitCheckout():
    global id_ls
    id_ls = update_lsbox()
    showID(id_ls)
    if not checkoutEntry.get().isdigit():
        checkoutEntry.delete(0, 'end')
        return messagebox.showinfo("Status", "please enter only number")

    global data_ls
    all_id = []

    data = read_Json("Data.json")
    for room in data:
        if room != "LastID":
            for items in data[room]["bookingData"]:
                all_id.append(items["id"])
    all_id = bubbleSort(all_id)

    if binarySearch(all_id, 0, len(all_id)-1, int(checkoutEntry.get())):
        room = getRoomByGuestID(int(checkoutEntry.get()))
        MsgBox = messagebox.askquestion(
            'Status', f'Are you sure you want checked out this room\nID : {room["id"]} room : {room["name"]}\nGuest : {room["Name"]} {room["Surname"]}', icon='warning')
        if MsgBox == 'yes':
            deleteData(room)
            checkoutEntry.delete(0, 'end')
            messagebox.showinfo("Status", "Check out successful")
    else:
        checkoutEntry.delete(0, 'end')
        messagebox.showinfo("Status", "ID not found :(")

    data_ls = update_data()
    update_table()


def update_table(data=None, tab=None, r=None):
    global data_ls
    if tab == None:
        tab = table
    if r == None:
        r = root
    for i in tab.get_children():
        tab.delete(i)
    r.update()
    row = 0
    if data == None:
        data_ls.clear()
        data_ls = update_data()
        data = data_ls
    for ele in data:
        table.insert(parent="",
                     index=row,
                     values=ele)
        row += 1


def binarySearch(arr, l, r, x):
    # result = binarySearch(arr, 0, len(arr)-1, target)
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return False


def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def showID(id_ls):
	# Clear the listbox
	id_list.delete(0, END)

	# Add toppings to listbox
	for item in id_ls:
		id_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
	# Delete whatever is in the entry box
	checkoutEntry.delete(0, END)

	# Add clicked list item to entry box
	checkoutEntry.insert(0, str(id_list.get(ANCHOR)).split(',')[0].replace("(","").replace("'",""))
    # checkoutEntry.insert(0, id_list.get(ANCHOR))
    

# Create function to check entry vs listbox
def check(e):
	# grab what was typed
	typed = checkoutEntry.get()

	if typed == '':
		data = id_ls
	else:
		data = []
		for item in id_ls:
			if typed in item[0]:
				data.append(item)

	# update our listbox with selected items
	showID(data)		

def ExitApplication():
    MsgBox = messagebox.askquestion(
        'Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()

def update_lsbox():
    global data_ls,id_ls
    id_ls.clear()
    for ele in data_ls:
        temp = []
        temp.append(str(ele[data_key.index('id')]))
        temp.append('Name : '+str(ele[data_key.index('Name')])+' | Surname : '
                    +str(ele[data_key.index('Surname')])+' | Room ID : '
                    +str(ele[data_key.index('roomID')]))
        id_ls.append(temp)
    return id_ls

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
    checkin_Frame = Frame(root, background='#ffdead')
    guestList_Frame = Frame(root, background='#c0dead')
    checkout_Frame = Frame(root, background='#80dead')
    menu_Frame.grid(row=0, column=1, sticky='ne')
    checkin_Frame.grid(row=0, column=0, sticky='nsew')
    guestList_Frame.grid(row=0, column=0, sticky='nsew')
    checkout_Frame.grid(row=0, column=0, sticky='nsew')

    # ======================= Menu Frame code =================
    # welcome_message = Label(menu_Frame,
    #                         text="WELCOME",
    #                         width=600,
    #                         font="Cascadia 56",
    #                         pady=40).pack(padx=10, pady=10)

    checkinBtn = Button(menu_Frame,
                        text="▶CHECK IN",
                        font="Cascadia 15",
                        width=20,
                        background='#ffdead',
                        activebackground='#ffdead',
                        relief='flat',
                        command=lambda: show_frame(checkin_Frame)
                        ).pack()

    showGuestBtn = Button(menu_Frame,
                          text="👥GUEST LIST",
                          font="Cascadia 15",
                          width=20,
                          background='#c0dead',
                          activebackground='#c0dead',
                          relief='flat',
                          command=lambda: show_frame(guestList_Frame)
                          ).pack()

    checkOutBtn = Button(menu_Frame,
                         text="◀CHECK OUT",
                         font="Cascadia 15",
                         width=20,
                         background='#80dead',
                         activebackground='#80dead',
                         relief='flat',
                         command=lambda: show_frame(checkout_Frame)
                         ).pack()

    exitBtn = Button(menu_Frame,
                     text="EXIT",
                     font="Cascadia 15",
                     width=20,
                     background='#40dead',
                     activebackground='#40dead',
                     relief='flat',
                     command=ExitApplication
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
                         font="Cascadia 30 bold",
                         background='#ffdead',
                         pady=20,
                         width=20,
                         border=5
                         ).pack(padx=10, pady=10)

    nameLabel = Label(checkin_Frame,
                      text="Enter name :",
                      font="Cascadia 20",
                      background='#ffdead',
                      width=0,
                      border=5
                      ).place(x=50, y=100)

    nameEntry = Entry(checkin_Frame,
                      font="Cascadia 20",
                      width=15,
                      border=5
                      )
    nameEntry.place(x=220, y=100)

    sureNameLabel = Label(checkin_Frame,
                          text="Surname :",
                          font="Cascadia 20",
                          background='#ffdead',
                          width=20,
                          border=5
                          ).place(x=500, y=100)

    sureNameEntry = Entry(checkin_Frame,
                          font="Cascadia 20",
                          width=15,
                          border=5
                          )
    sureNameEntry.place(x=750, y=100)

    phoneLabel = Label(checkin_Frame,
                       text="Enter phone number:",
                       font="Cascadia 20",
                       background='#ffdead',
                       width=20,
                       border=5
                       ).place(x=20, y=180)

    phoneEntry = Entry(checkin_Frame,
                       font="Cascadia 20",
                       width=30,
                       border=5
                       )
    phoneEntry.place(x=350, y=180)

    roomLabel = Label(checkin_Frame,
                      text="Enter room type :",
                      font="Cascadia 20",
                      background='#ffdead',
                      width=0,
                      border=5
                      ).place(x=50, y=260)

    roomType = ["Normal", "Deluxe", "Twin"]
    roomTypeSelected = StringVar()
    roomTypeSelected.set(roomType[0])
    roomOptions = OptionMenu(checkin_Frame, roomTypeSelected,
                             *roomType)
    roomOptions.place(x=340, y=260)
    roomOptions.config(font="Cascadia 18",
                        relief=GROOVE)

    labelDateCheckin = Label(checkin_Frame,
                             text="Date check in :",
                             font="Cascadia 20",
                             background='#ffdead',
                             width=0,
                             border=5
                             ).place(x=50, y=340)

    dateCheckin = DateEntry(checkin_Frame, selectmode='day',
                            year=now.year, month=now.month, day=now.day)
    dateCheckin.place(x=290, y=350)

    labelDateCheckout = Label(checkin_Frame,
                              text="Date check out :",
                              font="Cascadia 20",
                              background='#ffdead',
                              width=0,
                              border=5
                              ).place(x=500, y=340)

    dateCheckout = DateEntry(checkin_Frame, selectmode='day',
                             year=now.year, month=now.month, day=now.day)
    dateCheckout.place(x=740, y=350)

    pleaseSelectRoomLabel = Label(checkin_Frame,
                                  text="Select room :",
                                  font="Cascadia 20",
                                  background='#ffdead',
                                  width=0,
                                  border=5
                                  ).place(x=50, y=420)

    roomSelectedVariable = StringVar()
    roomSelectedVariable.set("\"Not selected\"")
    selectedRoomEntry = Entry(checkin_Frame, state=DISABLED,
                              textvariable=roomSelectedVariable,
                              font="Cascadia 20", width=14,
                              border=5
                              ).place(x=220, y=420)

    selectRoomBtn = Button(checkin_Frame, 
                            text="Sel Room",
                            font="Cascadia 15", 
                            relief=GROOVE,
                            command=room_id_selected_command
                            ).place(x=500, y=420)

    clearInputBtn = Button(checkin_Frame, 
                            text="Clear input",
                            relief=GROOVE,
                            font="Cascadia 15", 
                            command=clear_input_command
                            ).place(x=565, y=520)

    checkin_submit_btn = Button(checkin_Frame,
                                text="SUBMIT",
                                font="Cascadia 15",
                                relief=GROOVE,
                                pady=20,
                                width=20,
                                command=handleSubmitData
                                ).place(x=400, y=600)

    # ======================= 2.SHOW GUEST LIST Frame Code ================
    data = read_Json('Data.json')
    amount_data = list(data.keys())
    data_key = ["id",
                "Name",
                "Surname",
                "tel",
                "roomType",
                "roomID",
                "dateIn",
                "dateOut"]
    data_ls = []
    data_ls = update_data()

    guestListLabel = Label(guestList_Frame,
                            text="GUEST LIST",
                            font="Cascadia 30 bold",
                            background='#c0dead',
                            pady=20,
                            width=20,
                            border=5
                            ).pack(side='top')

    table_Frame = Frame(guestList_Frame,
                        background='#c0dead')
    table_Frame.pack(fill=BOTH, expand=YES)

    table_scrollbarx = Scrollbar(table_Frame,
                                 orient='horizontal')
    table_scrollbarx.pack(side=BOTTOM, fill=X)
    # y
    table_scrollbary = Scrollbar(table_Frame,
                                 orient='vertical')
    table_scrollbary.pack(side=RIGHT, fill=Y)
    # init table
    table = ttk.Treeview(table_Frame,
                         yscrollcommand=table_scrollbary.set,
                         xscrollcommand=table_scrollbarx.set)

    table_scrollbary.config(command=table.yview)
    table_scrollbarx.config(command=table.xview)
    table['columns'] = ('User ID', 'Name', 'Surname', 'tel',
                        'Room Type', 'Room No.', 'Date in', 'Date out')
    table.column("#0", width=0, stretch=True)
    for col in table['columns']:
        table.column(col, anchor=CENTER, width=80)

    table.heading("#0", text='', anchor=CENTER)
    for col in table['columns']:
        if col == 'User ID':
            table.heading(col, text=col, anchor=CENTER,
                          command=lambda: sort_button_command('id'))
        elif col == 'Name':
            table.heading(col, text=col, anchor=CENTER,
                          command=lambda: sort_button_command('Name'))
        elif col == 'Surname':
            table.heading(col, text=col, anchor=CENTER,
                          command=lambda: sort_button_command('Surname'))
        elif col == 'Room No.':
            table.heading(col, text=col, anchor=CENTER,
                          command=lambda: sort_button_command('roomID'))
        elif col == 'Date in':
            table.heading(col, text=col, anchor=CENTER,
                          command=lambda: sortdate_button_command('dateIn'))
        elif col == 'Date out':
            table.heading(col, text=col, anchor=CENTER,
                          command=lambda: sortdate_button_command('dateOut'))
        elif col == 'tel':
            table.heading(col, text=col, anchor=CENTER,
                          command=lambda: sort_button_command('tel'))
        elif col == 'Room Type':
            table.heading(col, text=col, anchor=CENTER,
                          command=lambda: sort_button_command('roomType'))
        else:
            table.heading(col, text=col, anchor=CENTER)

    table.pack(fill=BOTH, expand=YES)

    row = 0
    for ele in data_ls:
        table.insert(parent="",
                     index=row,
                     values=ele)
        row += 1

    # ======================= 3.CHECK OUT Frame Code ================
    checkoutLabel = Label(checkout_Frame,
                            text="CHECK OUT",
                            font="Cascadia 30 bold",
                            background='#80dead',
                            pady=20,
                            width=20,
                            border=5
                            ).pack(padx=10, pady=10)

    checkoutLabel2 = Label(checkout_Frame,
                           text="Enter ID : ",
                           font="Cascadia 20",
                           background='#80dead'
                           ).place(x=150, y=150)
    q=StringVar()
    checkoutEntry = Entry(checkout_Frame,
                          font="Cascadia 20",
                          width=30,
                          border=5,
                          textvariable=q
                          )
    checkoutEntry.place(x=275, y=150)

    checkoutBtn = Button(checkout_Frame,
                         text='CHECK OUT',
                         font='Cascadia 15',
                         relief=GROOVE,
                         pady=20,
                         width=20,
                         command=handleSubmitCheckout
                         ).place(x=400, y=600)

    # Create a listbox
    id_list = Listbox(checkout_Frame,font='Cascadia 15',width=65,height=10)
    id_list.place(x=150,y=200)

    # Create a list of pizza toppings
    id_ls = []
    id_ls = update_lsbox()
    showID(id_ls)

    # Create a binding on the listbox onclick
    id_list.bind("<<ListboxSelect>>",fillout)

    # Create a binding on the entry box
    checkoutEntry.bind("<KeyRelease>",check)


    show_frame(checkin_Frame)

    root.mainloop()
