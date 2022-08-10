'''
3. Longest Substring Without Repeating Characters
Medium

27329

1176

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Accepted
3,668,596
Submissions
10,921,929
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if(len(s))==1:
            return 1
        
        # left and right are sliding window pointers
        left = maxLength = 0
        
        # holds the current index of repeated chars 
        usedChar={}
        
        for right, ch in enumerate(s):
            
            # checks if current ele is in usedchar AND if the last repeated
            # character is in the current subString(i.e., range of subString = left to right )
            if ch in usedChar and left<=usedChar[ch]:
                left=usedChar[ch]+1
            else:
                maxLength= max(maxLength, right-left+1)

            # updates the current position of the repeated ch
            usedChar[ch]=right
        
        return maxLength