'''
Task Details
    Platform: LeetCode
    Name: 28. Implement strStr()
    Link: https://leetcode.com/problems/implement-strstr/
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not str or len(needle) == 0:
            return 0
        
        needle_len = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1
        