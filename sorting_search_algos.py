# l = int(input("enter the length:"))
# print(l)
# arr = []
# for i in range(l):
#     ele = int(input("enter the value:"))
#     arr.append(ele)
# print(arr)
# arr = [17,5,3,8,2,1]
# print(arr)
def selection(arr):
    l = len((arr))
    for i in range(l-1):
        # mn = min(arr[i:])
        #mn_ind = arr.index(mn,i) #to make code run for duplicate values , i will specify from where to start finding
        mn_ind = i
        for j in range(mn_ind+1,l):
            if arr[j]<arr[mn_ind]:
                mn_ind = j

        if mn_ind != i:
            arr[i],arr[mn_ind] = arr[mn_ind],arr[i]
    return arr

def bubble(arr):
    l = len(arr)
    for i in range(l-1): #after each iteration the greatest element will be pushed to the end
        for j in range(l-i-1): # -i as the last element is at the correct positions
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

#Quicksort
def pivot_place(arr,left,right):
    pivot = arr[left]
    l = left+1
    r = right
    while True:
        while l<=r and arr[l]<=pivot:
            l+=1
        while l<=r and arr[r]>=pivot:
            r-=1
        if l>r:
            arr[left],arr[r] = arr[r],arr[left] #swapping the pivot and the left
            break
        else:
            arr[l],arr[r] = arr[r],arr[l]
    return r #returning the pivot index

def quicksort(arr,left,right):
    if left<right: #till both are not pointing to the same value
        p= pivot_place(arr,left,right)
        quicksort(arr,left,p-1)
        quicksort(arr,p+1,right)
    return arr


def mergesort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        arr1 = mergesort(arr[:mid])
        arr2 = mergesort(arr[mid:])
        i = 0
        j = 0
        k = 0
        arr = [0]*len(arr)
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr[k] = arr1[i]
                i+=1
                k+=1
            else:
                arr[k] = arr2[j]
                j+=1
                k+=1
        while i<len(arr1):
            arr[k] = arr1[i]
            k+=1
            i+=1
        while j<len(arr2):
            arr[k] = arr2[j]
            k+=1
            j+=1
    return arr

def insertionSort(arr):
    l = len(arr)
    for i in range(1,l):
        cur = arr[i]
        pos = i
        while arr[pos-1]>cur and pos>0: #the while loop will execute pos number of times
            arr[pos] = arr[pos-1]
            pos -= 1
        arr[pos] = cur
    return arr
arr = [2,4,6,9,23,31,46,77,81,92,98]
def binary(arr,target):
    ln = len(arr)
    l = 0
    r = ln-1
    while l<r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            l = mid+1
        else:
            r = mid-1
print(binary(arr,31))






# a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

