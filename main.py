from package import Stack
from package import Queue
from tkinter import *
from tkinter import ttk
import json

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
    global name_box,surname_box,roomType_box,roomId_box,date_box1,date_box2,room_type,room_id
    name = name_box.get()
    surname = surname_box.get()
    roomType = roomType_box.get()
    roomID = roomId_box.get()
    dat = [roomType_box.get(),roomId_box.get(),name_box.get(),surname_box.get(),date_box1.get(),date_box2.get()]
    key = ['Room_Type','Room_ID','Name','Surname','date_1','date_2']
    inp_data = {}
    for ele in range(len(key)):
        inp_data.update({key[ele] : dat[ele]})
    print(inp_data)


if __name__ == '__main__':
    ####################
    ### main is here ###
    ####################
    # example use of read_Json()
    data = read_Json('Data.json')
    room_type = list(data.keys())
    room_id = [list(data[i].keys()) for i in room_type]
    print(room_type,room_id)

    root = Tk()
    root.title('Book MEEE')
    root.geometry("1024x768")

    ###################
    ### --- Table Frame --- ###
    ###################
    table_Frame = LabelFrame(root, text="Data")
    table_Frame.pack(fill='both')

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

    table['columns'] = ('Room Type', 'Room ID', 'Date00', 'Date01', 'Date02', 'Date03', 'Date04', 'Date05', 'Date06',
                        'Date07', 'Date08', 'Date09', 'Date10')

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
    roomType_box = Entry(room_Frame, bd=3, width=20)
    roomId_label = Label(room_Frame,text="Room ID : ")
    roomId_box = Entry(room_Frame,bd=3,width=20)
    date_label1 = Label(date_Frame,text='From ')
    date_label2 = Label(date_Frame,text='   -   ')
    date_box1 = Entry(date_Frame,bd=3,width=30)
    date_box2 = Entry(date_Frame,bd=3,width=30)
    Book_button = Button(date_Frame, text='Book',command=get_book)


    roomType_label.pack(side='left',padx=10)
    roomType_box.pack(side='left')
    roomId_label.pack(side='left',padx=10)
    roomId_box.pack(side='left')
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


