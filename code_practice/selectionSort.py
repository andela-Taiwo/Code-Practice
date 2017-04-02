
def selectionSort(alist):

    for fillslot in range(len(alist)-1, 0,-1):
        maxPosition= 0
        for i in range(1,fillslot+1):
            if alist[i]>alist[maxPosition]:
                maxPosition = i
        temp = alist[fillslot]
        alist[fillslot] = alist[maxPosition]
        alist[maxPosition ]= temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
