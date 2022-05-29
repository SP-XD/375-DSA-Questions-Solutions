"""
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
"""

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        """
        #1st approach
        #time limit execeeded
        repeated=0
        missing=0
        temp_r=0
        temp_m=0
        f2=0
        f3=0

        for i in range(len(A)):
            c=0
            f=0

            for j in range(len(A)):
                if A[i]==A[j]:
                    c+=1
                    temp_r=A[i]
                if (i+1)==A[j]:
                    f=1
                    
                
            if c>1:
                repeated=temp_r
                f2=1
            if f==0:
                missing=i+1
                f3=1
            if(f2==1 and f3==1):
                break
        
        #2nd approach
        #overflow
        sum_n=0
        sum_actual=0
        sum_square_n=0
        sum_square_actual=0

        for i in range(len(A)):
            sum_n+=i
            sum_actual+=A[i]
            sum_square_n+=i**2
            sum_square_actual+=A[i]**2

        equation1=((sum_n-sum_actual)+(sum_square_n-sum_square_actual))
        repeated=equation1//2
        missing=equation1-repeated

        #3rd approach
        n = len(A)
        x = sum(A) - sum(set(A))
        k =  int(n*(n+1)/2)-sum(A)
        print(k)
        return [x,x+k]

        a=[1,2,3,3,5]
        print(repeatedNumber(a))

       """
        A=sorted(A)
        repeated=0
        missing=1
        f=0
        for i in range(len(A)-1):
            if A[i]==A[i+1]:
                repeated=A[i]
            #addition of 1s till the missing index will return the missing number
            if missing==A[i]:
                missing+=1

        #corner case
        #missing number is in last index
        if missing==0:
            missing=len(A)
        return [repeated,missing]