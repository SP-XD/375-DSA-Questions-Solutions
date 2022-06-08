"""
Given a sorted and rotated array, find if there is a pair with a given sum

Difficulty Level : Medium
Last Updated : 13 Jul, 2021
Given an array that is sorted and then rotated around an unknown point. Find if the array has a pair with a given sum ‘x’. It may be assumed that all elements in the array are distinct.

Examples : 

Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
Output: true
There is a pair (6, 10) with sum 16

Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
Output: true
There is a pair (26, 9) with sum 35

Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
Output: false
There is no pair with sum 45.
"""

def rotatedArraySumPair(arr: list, n: int, x: int)-> list:

	#finding the pivot element using linear search, which can be optimized to binary search	
	for i in range(0, n-1):
		if(arr[i]>arr[i+1]):
			break	

	#two pointer approach		
	#lowest element or the pivot + 1 element
	p1=(i+1)%n # %n resets p1 to index 0 when p1 overflows length of array 
	#largest element or the pivot element
	p2=i

	while( p1!=p2):

		if arr[p1]+arr[p2]==x:
			return [arr[p1], arr[p2]]

		if arr[p1]+arr[p2]>x:
			p2=(n+p2-1)%n
		else:	
			p1=(p1+1)%n


	return [-1] 

n=int(input("Enter the length of the array: "))

arr=[]

for i in range(n):
	element=int(input("Enter the element: "))
	arr.append(element)

x=int(input("Enter the sum pair to be found: "))

print("Sum found:", rotatedArraySumPair(arr, n, x))
