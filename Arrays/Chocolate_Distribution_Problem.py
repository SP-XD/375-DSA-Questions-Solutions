#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        # code here
        A.sort()
        #largest number of chocolates
        min_diff=A[N-1]-A[0]
        max_packets=0
        min_packets=0
        #print(*A) 
        for i in range(N):
            min_packets=A[i]
            #when the number of students is equal to the number of total packets
            if(N==M):
                max_packets=A[N-1]
                #print("diff=", max_packets-min_packets )
                min_diff=min(min_diff, max_packets-min_packets )

            #when the number of students is less than the number of total packets
            if(i+M-1<N):
                max_packets=A[i+M-1]
                #print("diff=", max_packets-min_packets )
                min_diff=min(min_diff, max_packets-min_packets )
           
        """
        #easier solution 
        # running loop till (len of array - number of students) 
        # if m is equal to n then min_diff is already calculated
        for i in range(N-M+1):
            min_diff=min(min_diff, A[i+M-1]-A[i])
        """
        return min_diff
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends