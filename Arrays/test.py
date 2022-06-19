from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    low=0
    mid=0
    high=len(arr)-1
    
    while(mid<=high):
        if arr[mid]==0:
            arr[mid], arr[low]=arr[mid],arr[low]
            low+=1
            mid+=1
        else if arr[mid]==1:
            arr[mid]+=1
        else if arr[mid]==2:
            arr[high], arr[mid]=arr[mid], arr[high]
            high-=1
            mid+=1


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
