""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""

def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.


    fruits = open(filename)
    list_of_contents = fruits.read().split("\n")

    fruits.close()

    return list_of_contents


def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """
    for value in list1:
        if value == list2:
            print value

#for fruits in list_of_contents:
    #if fruits.compare()
        #print "{} are on both lists".format(fruits)
#for value in compare("fruits_1.txt","fruits_2.txt")
#print value

#for fruits in open_and_read_file("fruits_1.txt"):
        #print fruits

#for fruits in open_and_read_file("fruits_2.txt"):
        #print fruits
