#insertion sort python
import time
import random as r
import os

arr=[]

for i in range(0, 10):
    arr.append(r.randint(1, 10))

print(arr)

def insertion(array):
    n = len(array)
    for i in range(1, n):
        x = i-1
        while x >= 0 and i < array[x]:
            array[x+1] = array[x]
            x -= 1
        array[x+1] = i
        print(array)
    print(array)

#DOESNT WORK DONT TRUST THIS IT REPLACES NUMBERS AAAAAAAAA
insertion(arr)