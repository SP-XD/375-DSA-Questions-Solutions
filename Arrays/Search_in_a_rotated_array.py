#User function Template for python3

class Solution:
    
    def binarySearch(self, A : list, l : int, h : int, key : int):
        index=-1
        while(l<=h):
            pivot=l+(h-l)//2
            
            if key==A[pivot]:
                index=pivot
                return index
    
            if key<A[pivot]:
                h=pivot-1
            elif key>A[pivot]:
                l=pivot+1
    
        
        return index
        
    def findPivot(self, A : list, n : int):
        #finding the pivot point of the rotated array
        # with linear search
        for i in range(n-1):
            if A[i+1]<A[i]:
                return i
        
        return -1
        
    def search(self, A : list, l : int, h : int, key : int):
        # Complete this function
        pivot=self.findPivot(A, len(A))

        #print(A[pivot]) 

        if pivot==-1:
            return self.binarySearch(A, l, h, key)
        else:
            if key==A[pivot]:
                return pivot
            # if the starting element is less than key then search in the first half
            # further explanation: as the array is sorted but rotated at some index later, the starting 
            # element will be less the key if it exists in the first sub array
            if  A[0] <=key :
                return self.binarySearch(A, 0, pivot, key)
            
            return self.binarySearch(A, pivot+1, h, key )
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends