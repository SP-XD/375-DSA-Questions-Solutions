"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        n=len(nums) 
        #approach is calculating the left and right sides separately and storing the product of boh left and right and storing in answer array
        #calculating the product of left sides and storing in ans 
        left=1
        for i in range(n):
            if i > 0:
                left*=nums[i-1]
            ans[i]=left
        
        #calculating the product of right sides and again finding the product & storing in ans 
        right=1
        for i in reversed(range(0,n)):
            if i < n-1:
                right*=nums[i+1]
            ans[i]*=right
        
        return ans