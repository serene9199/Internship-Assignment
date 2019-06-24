#1. Write a program to insert an element into an array to the nth position

#! /usr/bin/python
lst=[]
# Enter the number of elemetns as input 
size = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, size): 
    e = int(input()) 
    lst.append(e) # adding the element
    
n = int(input("Enter the position:")) 
p = int(input("Enter the element to be inserted:")) 

lst = lst[:n] + [p] + lst[n:] 
print(lst)

