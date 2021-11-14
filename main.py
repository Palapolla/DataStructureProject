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



if __name__=='__main__':
    ####################
    ### main is here ###
    ####################
    
    root = Tk()
    root.title('Book MEEE')
    root.geometry("800x400")

        ########################
    ### Buttons & text boxs zone ###
        ########################
    Search_box = Entry(root,bd=3,width=30)
    Search_box.grid(row=0,column=2,sticky="ne")
    Book_button = Button(text='Book')
    Book_button.grid(row=0,column=2,sticky="nw")
    Search_button = Button(text='Search')
    Search_button.grid(row=0,column=2,sticky="ne")
    

    table_Frame = Frame(root)
    table_Frame.grid(row=0,column=0,sticky="nw")

    table = ttk.Treeview(table_Frame)
    table['columns'] = ('Room Type', 'Room ID', 'Date00', 'Date01', 'Date02', 'Date03', 'Date04', 'Date05')

    table.column("#0", width=0,  stretch=True)
    for col in table['columns']:
        table.column(col,anchor=CENTER, width=80)

    table.heading("#0",text="",anchor=CENTER)
    for col in table['columns']:
        table.heading(col,text=col,anchor=CENTER)

    table.pack()

    # make objet position relate to window size
    # row & column of Tkinter 
    # col = [0,1,2]
    # row = [0,1,2,3]
    
    element_list = [Book_button,Search_button,Search_box]
    
    row_num = 0
    for ele in element_list:
        root.grid_rowconfigure(row_num,weight=1)
        row_num += 1
    
    col_num = 0
    for ele in element_list:
        root.grid_columnconfigure(col_num,weight=1)
        col_num += 1

    root.mainloop()