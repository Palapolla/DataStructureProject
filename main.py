from package import Stack
from package import Queue
from tkinter import *
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