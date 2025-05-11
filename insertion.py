#insertion sort python
import time
import random as r
import os

arr=[]

maxnum = int(input("maximum number? "))
slep = input("slep? (enter if no) ")
amount = int(input("list amount? "))
for i in range(0, amount):
    arr.append(r.randint(1, maxnum))

print(len(arr))
print(arr)
print(arr[2])
print(arr[6])
print(arr[1])

def insertion(array):
    global maxnum
    global slep
    counter = 0
    loadarray = ["loading.", "loading..", "loading..."]
    a=0
    if not(slep):
        print(loadarray[a])
    result = [maxnum+1]
    for i in range(0, len(array)):
        for x in range(0, len(result)):
            counter += 1
            #print("a")
            #print(x)
            if result[x] > array[i]:
                result.insert(x, array[i])
                break
        if slep:
            os.system("clear")
            print("result:", result)
            time.sleep(0.05)
        else:
            if counter > amount*100:
                a+=1
                if a > 2:
                    a=0
                os.system("clear")
                print(loadarray[a])
                counter = 0
        #print("orig:", array)
    result.pop(-1)
    return result


print(insertion(arr))