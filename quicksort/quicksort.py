import random

def quicksort(mylist, lowIndex, highIndex):
    if highIndex > lowIndex:
        p = partition(mylist, lowIndex, highIndex)
        quicksort(mylist, lowIndex, p-1)
        quicksort(mylist, p+1, highIndex)

def partition(mylist, lowIndex, highIndex):
    divider = lowIndex
    pivot = highIndex

    for i in range(lowIndex, highIndex):
        if(mylist[i] < mylist[pivot]):
            mylist[i], mylist[divider] = mylist[divider], mylist[i]
            divider += 1

    mylist[pivot], mylist[divider] = mylist[divider], mylist[pivot]

    return divider


mylist = random.sample(range(1, 9999999), 10000)
quicksort(mylist, 0, 9999)
print(mylist)
