class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_max=nums[0] 
        sum_temp=nums[0]

        if len(nums)==1:
            return nums[0]
        
        for i in nums[1:]:
            sum_temp=max(sum_temp+i, i)
            sum_max=max(sum_max, sum_temp)
        
        """
        #alternative
        #kadane's algorithm
        sum_max=nums[0]
        sum_cur=0
         
        for i in nums:
            sum_cur+=i 
            if(sum_cur>sum_max):
                sum_max=sum_cur
            if(sum_cur<0):
                sum_cur=0
        return sum_max  
        """
        return sum_max