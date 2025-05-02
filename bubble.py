#bubble sort python
import time
import random as r
import os

arr=[]

for i in range(0, 1000):
    arr.append(r.randint(1, 1000))

print(arr)

def bubble(array):
    swaps = 0
    i=0
    holder = 0
    a = 0
    length = len(array)
    while True:
        if i+1 < length:
            if array[i] > array[i+1]:
                holder = array[i]
                array[i] = array[i+1]
                array[i+1] = holder
                swaps += 1
                os.system("clear")
                print(array)
        elif i == length:
            i = 0
            if swaps == a:
                break
            a = swaps
            continue
        #time.sleep(0.01)
        i+=1
    print(array)
    print(swaps)

bubble(arr)