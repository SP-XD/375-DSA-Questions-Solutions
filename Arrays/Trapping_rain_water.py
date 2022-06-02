"""
42. Trapping Rain Water
Hard

18647

263

Add to List

Share
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105`
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0; right=n-1
        maxleft=0; maxright=0
        units_of_water=0
        
        while(left<=right):
            if(height[left]<=height[right]):
                if(height[left]>=maxleft):
                    maxleft=height[left]
                else: 
                    units_of_water+=maxleft-height[left]
                left+=1
            else:
                if(height[right]>=maxright):
                    maxright=height[right]
                else:
                    units_of_water+=maxright-height[right]
                right-=1
        
        return units_of_water
           