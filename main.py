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
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1

        # We have either reached the beginning of the array or we have found
        # an element of the sorted array that is smaller than the element
        # we're trying to insert at index currentPosition - 1.
        # Either way - we insert the element at currentPosition
        array[currentPosition] = currentValue

def read_Json(filename):
    with open(filename) as file:
        data = json.load(file)
    print(data)
    return data
    # return data as dict in dict in dict in ...


if __name__=='__main__':
    ####################
    ### main is here ###
    ####################
    

    # example use of read_Json()
    data = read_Json('Data.json')
    print(data)

    root = Tk()
    root.title('Book MEEE')
    root.geometry("1024x768")

        ###################
    ### --- Table Frame --- ###
        ###################
    table_Frame = LabelFrame(root,text="Data")
    table_Frame.pack(fill='both')

    # scrollbar
    # x
    table_scrollbarx = Scrollbar(table_Frame,orient='horizontal')
    table_scrollbarx.pack(side=BOTTOM, fill=X)
    # y
    table_scrollbary = Scrollbar(table_Frame,orient='vertical')
    table_scrollbary.pack(side= RIGHT,fill=Y)

    # table datas
    table = ttk.Treeview(table_Frame,yscrollcommand=table_scrollbary.set, xscrollcommand =table_scrollbarx.set)
    table['columns'] = ('Room Type', 'Room ID', 'Date00', 'Date01', 'Date02', 'Date03', 'Date04', 'Date05', 'Date06',
                        'Date07', 'Date08', 'Date09', 'Date10')
    
    table_scrollbary.config(command=table.yview)
    table_scrollbarx.config(command=table.xview)

    # define column
    table.column("#0", width=0,  stretch=True)
    for col in table['columns']:
        print(col)
        table.column(col,anchor=CENTER, width=80)
    # create heading
    table.heading("#0",text="",anchor=CENTER)
    for col in table['columns']:
        table.heading(col,text=col,anchor=CENTER)
    # insert by table.insert(parent='',index='',iid=,text='', values=())

    table.pack()

        #####################
    ### --- search Frame --- ###
        ####################
    search_Frame=LabelFrame(root,text="search")
    search_Frame.pack(fill='both')

    # Search frame's elements
    Search_button = Button(search_Frame,text='Search')
    Search_box = Entry(search_Frame,bd=3,width=30)

    Search_box.pack(side='left',padx=10,pady=10)
    Search_button.pack(side='left')


    book_Frame = LabelFrame(root,text="book")
    book_Frame.pack(fill="both",expand='yes')
    Book_button = Button(book_Frame,text='Book')
    Book_button.pack()


    root.mainloop()
