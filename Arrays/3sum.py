"""
15. 3Sum
Medium

18222

1753

Add to List

Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
Accepted
1,990,175
Submissions
6,361,953
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        linearly moving in i index and finding the other two values using the two pointer approach  
        """ 
        triplets=[]
        nums.sort() 
        for i in range(len(nums)-2):
            # if first element is greater than 0 then no triplets can form a sum of zero
            if nums[0]>0:
                break
            
            if i==0 or (i>0 and nums[i]!=nums[i-1]):
                #two pointers
                left=i+1
                right=len(nums)-1
                sum=0-nums[i]
                while(left<right):
                    
                    if nums[left]+nums[right]==sum:
                        triplets.append([nums[i], nums[left], nums[right]]) 
                    
                        #skipping duplicates
                        while (left<right and nums[left]==nums[left+1]):
                            left+=1
                        while (left<right and nums[right]==nums[right-1]):
                            right-=1
                    if nums[left]+nums[right]>sum:
                        right-=1
                    else:
                        left+=1
        return triplets