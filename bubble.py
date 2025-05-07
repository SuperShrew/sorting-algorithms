#bubble sort python
import time
import random as r
import os

arr=[]

b = int(input("list amount? "))
c = int(input("list range? "))

for i in range(0, b):
    arr.append(r.randint(1, c))

print(arr)

a = int(input("print after pass (1) or after swap (2)"))

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
                if a == 2:
                    os.system("clear")
                    print(array)
        elif i == length:
            os.system("clear")
            print(array)
            i = 0
            if swaps == a:
                break
            a = swaps
            continue
        #time.sleep(0.05)
        i+=1
    print(array)
    print(swaps)

bubble(arr)