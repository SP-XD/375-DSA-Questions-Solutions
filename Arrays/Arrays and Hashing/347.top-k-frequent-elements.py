#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (64.92%)
# Likes:    10764
# Dislikes: 409
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        #Brute Force Approach: 
        #1. create a hashtable of i elements and its freq. 
        #2. find the max freq and then remove that max element from hashtable after adding it to result in each iteration

        hashmap=collections.Counter(nums)
        res=[]
        maxFreq=0
        while (k>0):
            for i in hashmap:
                if hashmap[maxFreq]<hashmap[i]:
                    maxFreq=i
            res.append(maxFreq) 
            hashmap.pop(maxFreq)
            k-=1
            maxFreq=0

        return res 
        ''' 

        '''
        Bucket approach: 
        Eg: (1,1,1,2,2,3)  k=2

        i(count) = | 0  | 1   | 2   | 3   |  
        value =    | [] | [3] | [2] | [1] |

        output : k=[1,2]
        '''

        count={}
        freq=[[] for i in range(len(nums)+1)]    #empty 2d array of nums len 
                                                #len+1 cause array starts at 0 index and its a corner case

        for n in nums:                          #counting the freq of each element
            count[n]=1+count.get(n, 0)

        for n, c in count.items():              #amending key element n at Value index (i.e, count itself is the index)
            freq[c].append(n)

        res=[]
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)                   #appending all elements of freq[i],     
                                                #here is a catch, this particular problem mentioned all freq of numbers is unqiue but this solution also takes into consideration the possibility of multiple same freq of a number 
                if len(res)==k:                 #when res is same len as k, return res
                    return res
        

# @lc code=end

