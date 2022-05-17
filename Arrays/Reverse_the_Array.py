#User function Template for python3

def reverseWord(s):
    #your code here
    '''
    reversedString=''
    
    for i in s:
        reversedString=i + reversedString
        
    return reversedString
    '''

    #python solution 
    return s[::-1]
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends
