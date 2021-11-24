from package import Queue
from package import Stack
from package import Calendar
from package import DoublyLinkedList
from tkinter import *
from tkinter import ttk
import json
import datetime

# Pay respect to the Buddha before coding
#                            _
#                         _ooOoo_
#                        o8888888o
#                        88" . "88
#                        (| -_- |)
#                        O\  =  /O
#                     ____/`---'\____
#                   .'  \\|     |//  `.
#                  /  \\|||  :  |||//  \
#                 /  _||||| -:- |||||_  \
#                 |   | \\\  -  /'| |   |
#                 | \_|  `\`---'//  |_/ |
#                 \  .-\__ `-. -'__/-.  /
#               ___`. .'  /--.--\  `. .'___
#            ."" '<  `.___\_<|>_/___.' _> \"".
#           | | :  `- \`. ;`. _/; .'/ /  .' ; |
#           \  \ `-.   \_\_`. _.'_/_/  -' _.' /
# ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
#                         `=--=-'                    hjw
# if satu 99:
#   bug = 0

# ref. https://stackabuse.com/insertion-sort-in-python/
def insertion_sort(array):
    # We start from 1 since the first element is trivially sorted
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        # As long as we haven't reached the beginning and there is an element
        # in our sorted array larger than the one we're trying to insert - move
        # that element to the right
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        array[currentPosition] = currentValue



    #  "Room Type":{
    #     "Room Number":{
    #         "Name":"A",
    #         "Time":"B",
    #         "total_cost":"C"
    #     },
def read_Json(filename):
    with open(filename) as file:
        data = json.load(file)

    return data
    # return data as dict in dict in dict in ...

def get_search_button():
    global Search_box,text_box
    message = Search_box.get()
    print(message,type(message))
    text_box.delete(1.0,"end")
    text_box.insert(1.0, message)

def get_book():
    global name_box,surname_box,room_type_selected,room_ID_selected,date_box1,date_box2,room_type,room_id
    dat = [room_type_selected.get(),room_ID_selected.get()
            ,name_box.get(),surname_box.get()
            ,date_box1.get(),date_box2.get()]
    key = ['Room_Type','Room_ID','Name','Surname','date_1','date_2']

    inp_data = {}

    for ele in range(len(key)):
        inp_data.update({key[ele] : dat[ele]})
    print(inp_data)
    data = read_Json('Data.json')

def next_page(): 
    global table,table_page,max_tab_page,column,static_col,page_label
    if table_page+1 < max_tab_page:
        print('Next page clicked')
        table_page += 1
        print('table_page',table_page)
        print('max',max_tab_page)
        table['columns'] = tuple(static_col+column[table_page])
        # define column
        table.column("#0", width=0,  stretch=True)
        for col in table['columns']:
            table.column(col, anchor=CENTER, width=80)
        # create heading
        table.heading("#0", text="", anchor=CENTER)
        for col in table['columns']:
            table.heading(col, text=col, anchor=CENTER)
        # insert by table.insert(parent='',index='',iid=,text='', values=())
    page_label.config(text='{}/{}'.format(table_page+1,max_tab_page))
    page_label.pack()
    table.pack()

def prev_page():
    global table,table_page,max_tab_page,column,static_col,page_label
    if table_page-1 >= 0:
        print('Previous page clicked')
        table_page -= 1
        print('table_page',table_page)
        print('max',max_tab_page)
        table['columns'] = tuple(static_col+column[table_page])
        # define column
        table.column("#0", width=0,  stretch=True)
        for col in table['columns']:
            table.column(col, anchor=CENTER, width=80)
        # create heading
        table.heading("#0", text="", anchor=CENTER)
        for col in table['columns']:
            table.heading(col, text=col, anchor=CENTER)
        # insert by table.insert(parent='',index='',iid=,text='', values=())
    page_label.config(text='{}/{}'.format(table_page+1,max_tab_page))
    page_label.pack()
    table.pack()


def get_roomType_dropdown(choice):
    global room_type_selected,r_type_index,room_ID_selected,room_id,roomId_drop
    choice = room_type_selected.get()
    print('Room_type',choice)

def get_roomID_dropdown(choice):
    global room_ID_selected
    choice = room_ID_selected.get()
    print('Room_ID',choice)


    # ################################## #
    # ---------------------------------- #
    # ---------------------------------- #
    # ---------- main is here ---------- #
    # ---------------------------------- #
    # ---------------------------------- #
    # ################################## #
    
if __name__ == '__main__':

# problems
#   * Datas table very laggy // low performance
#       Hypothesis : "CPU Thread"
#       Solution :  import threading to config the cpu thread
#                   or 1 page per 1 month
    Dll_calendar = DoublyLinkedList()
    # calend = Calendar()
    # calend.one_month_calendar(1)
    # print(calend.Calendar)
    for mon in range(1,13,1):
        # print(mon)
        calend = Calendar()
        Dll_calendar.append(calend.one_month_calendar(mon))
    print(Dll_calendar)
    # print(Dll_calendar.get(1).data.Calendar)



    # example use of read_Json()
    data = read_Json('Data.json')
    room_type = list(data.keys())
    room_id = [list(data[i].keys()) for i in room_type]
    # print(room_type,room_id)

    root = Tk()
    root.title('Book MEEE')
    root.geometry("1024x768")


    ###########################
    ### --- Table Frame --- ###
    ###########################
    table_page = 0
    max_tab_page = len(Dll_calendar)

    table_Frame = LabelFrame(root, text="Data")
    table_Frame.pack(fill='both')
    tab_butt_Frame = Frame(table_Frame)
    
    page_label = Label(tab_butt_Frame,text='{}/{}'.format(table_page+1,max_tab_page))
    next_button = Button(tab_butt_Frame, text='>',command=next_page)
    prev_button = Button(tab_butt_Frame, text='<',command=prev_page)


    # scrollbar
    # x
    table_scrollbarx = Scrollbar(table_Frame, orient='horizontal')
    table_scrollbarx.pack(side=BOTTOM, fill=X)
    # y
    table_scrollbary = Scrollbar(table_Frame, orient='vertical')
    table_scrollbary.pack(side=RIGHT, fill=Y)

    # table datas
    table = ttk.Treeview(
        table_Frame, yscrollcommand=table_scrollbary.set, xscrollcommand=table_scrollbarx.set)

    table_scrollbary.config(command=table.yview)
    table_scrollbarx.config(command=table.xview)

    # add date to table
    table['columns'] = ('Room Type', 'Room ID')
    static_col = list(table['columns'])
    column = []
    for ele in range(len(Dll_calendar)):
        column.append(Dll_calendar.get(ele).data.Calendar)
    # column = column + calend
    print('len(col)',len(column))
    table['columns'] = tuple(static_col+column[table_page])


    # define column
    table.column("#0", width=0,  stretch=True)
    for col in table['columns']:
        table.column(col, anchor=CENTER, width=80)
    # create heading
    table.heading("#0", text="", anchor=CENTER)
    for col in table['columns']:
        table.heading(col, text=col, anchor=CENTER)
    # insert by table.insert(parent='',index='',iid=,text='', values=())

    table.pack()
    tab_butt_Frame.pack(anchor='se')
    next_button.pack(side='right')
    page_label.pack(side='right')
    prev_button.pack(side='right')

    # insert datas to table
    insert = 0
    for r_type in range(len(room_type)):
        for r_id in range(len(room_id)+1):
            # print(r_id,len(room_id))
            # print('insert',room_type[r_type],room_id[r_type][r_id])
            table.insert(parent="", index=insert, values=(
                room_type[r_type], room_id[r_type][r_id]))
            insert += 1

        #####################
    ### --- search Frame --- ###
        ####################
    search_Frame = LabelFrame(root, text="search",padx=100)
    searchbox_Frame = Frame(search_Frame)
    result_Frame = Frame(search_Frame)
    search_Frame.pack(fill='both',expand=NO)
    searchbox_Frame.pack(side='right',expand=YES)
    result_Frame.pack(side='left',expand=YES)

    # Search frame's elements
    Search_button = Button(searchbox_Frame, text='Search',command=get_search_button)
    Search_box = Entry(searchbox_Frame, bd=3, width=30)



    text_box = Text(result_Frame,height=12)

    text_box.pack(side='left',padx=10,pady=10)
    Search_box.pack(side='left')
    Search_button.pack(side='left',padx=10)

        #####################
    ### ---- Book Frame ---- ###
        ####################
    book_Frame = LabelFrame(root, text="book",padx=100,pady=50)
    book_Frame.pack(fill="both", expand='yes')
    name_Frame = Frame(book_Frame)
    name_Frame.pack(fill=BOTH,pady=10)
    room_Frame = Frame(book_Frame)
    room_Frame.pack(fill=BOTH,pady=10)
    date_Frame = Frame(book_Frame)
    date_Frame.pack(fill=BOTH,pady=10)

    name_label = Label(name_Frame,text='Name : ')
    name_box = Entry(name_Frame, bd=3, width=30)

    surname_label = Label(name_Frame,text="Surname : ")
    surname_box = Entry(name_Frame,bd=3,width=30)

    roomType_label = Label(room_Frame,text='Room Type : ')
    room_type_selected = StringVar()
    room_type_selected.set(room_type[0])
    roomType_drop = OptionMenu(room_Frame,room_type_selected,*room_type,command=get_roomType_dropdown)

    roomId_label = Label(room_Frame,text="Room ID : ")
    room_ID_selected = StringVar()
    room_ID_selected.set(room_id[0][0])
    roomId_drop = OptionMenu(room_Frame,room_ID_selected,*room_id[0],command=get_roomID_dropdown)

    date_label1 = Label(date_Frame,text='Date : ')
    date_label2 = Label(date_Frame,text='   -   ')
    date_box1 = Entry(date_Frame,bd=3,width=30)
    date_box2 = Entry(date_Frame,bd=3,width=30)

    Book_button = Button(date_Frame, text='Book',command=get_book)


    roomType_label.pack(side='left')
    roomType_drop.pack(side='left')
    roomId_label.pack(side='left')
    roomId_drop.pack(side='left')
    name_label.pack(side='left')
    name_box.pack(side='left',padx=10)
    surname_label.pack(side='left')
    surname_box.pack(side='left',padx=10)
    date_label1.pack(side='left')
    date_box1.pack(side='left')
    date_label2.pack(side='left')
    date_box2.pack(side='left')
    Book_button.pack(side='left',padx=10)



    root.mainloop()


    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    # ░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
    # ░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
    # ░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
    # ░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
    # ░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
    # ░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
    # ░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
    # ░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
    # ░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
    # ░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
    # ░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
    # ░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
    # ░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
    # ░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
    # ░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
    # ░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
    # ░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
    # ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░



