#import collections

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return len(nums)!=len(set(nums))

        """
        #alternate solution
        map1= collections.Counter(nums)
        
        for i in map1:
            if map1[i] > 1:
                return True
            
        return False
        """
        