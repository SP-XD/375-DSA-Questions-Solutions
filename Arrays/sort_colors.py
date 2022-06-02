"""
75. Sort Colors
Medium

10110

422

Add to List

Share
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 
"""
class Solution:
    def sortColors(self, arr: List[int]) -> None:
        low=0
        mid=0
        high=len(arr)-1
        #using dutch flag algorithm
        while (mid<=high):
            if arr[mid]==0:
                arr[mid], arr[low]=arr[low],arr[mid]
                low+=1
                mid+=1
            elif arr[mid]==2:
                arr[mid], arr[high]=arr[high], arr[mid]
                high-=1
            else:
                mid+=1
                