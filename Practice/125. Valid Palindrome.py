'''
Task Details
    Platform: LeetCode
    Name: 125. Valid Palindrome 
    Link: https://leetcode.com/problems/valid-palindrome/
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while (i<j):
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            while i<j and not s[i].isalnum():
                i += 1
            while j>i and not s[j].isalnum():
                j -= 1
        return True
