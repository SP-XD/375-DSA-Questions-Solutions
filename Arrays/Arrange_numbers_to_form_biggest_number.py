'''
Arrange given numbers to form the biggest number | Set 1

Difficulty Level : Medium
Last Updated : 01 Jul, 2022
Given an array of numbers, arrange them in a way that yields the largest value. For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value. And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
A simple solution that comes to our mind is to sort all numbers in descending order, but simply sorting doesn’t work. For example, 548 is greater than 60, but in output 60 comes before 548. As a second example, 98 is greater than 9, but 9 comes before 98 in output.

So how do we go about it? The idea is to use any comparison based sorting algorithm. 
In the used sorting algorithm, instead of using the default comparison, write a comparison function myCompare() and use it to sort numbers.

'''
 
def compareDigitSort(array: list):
    l=len(array)
    
    if l==1:
        return array[0]

    #converting int -> string numbers 
    for i in range(l):
        array[i]=str(array[i])
      
    for i in range(l):
        for j in range(l-1-i):
            #comparing in lexicographical order as number is in string format
            # 'a' > 'b' = false , '2' > '1' = true
            if array[j+1]>array[j]:
                array[j], array[j+1] = array[j+1], array[j]

    biggestNumber=''.join(array)

    #corner case where all number are zeros
    if (biggestNumber=='0'*l):
        return 0

    return biggestNumber

array=[54, 546, 548, 60]
print("The biggest number is ", compareDigitSort(array))