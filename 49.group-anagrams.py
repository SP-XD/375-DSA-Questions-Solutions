#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (65.24%)
# Likes:    11206
# Dislikes: 358
# Total Accepted:    1.5M
# Total Submissions: 2.4M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams_res=[] 

        hashmap={}

        for s in strs:
            count=[0]*26                     # a....z counter array which is initialized with 0  

            for c in s:
                count[ord(c)-ord('a')]+=1   #store the frequency of chars from s 

            hash=tuple(count)
            
            if hashmap.get(hash)!=None:     #if hash is already present (i.e, no keyError) then append s
                hashmap[hash].append(s)
            else:                           #else add new hash and initialise s
                hashmap[hash]=[s]

        anagrams_res=hashmap.values()

        return anagrams_res
# @lc code=end