'''
Task Details
    Platform: LeetCode
    Name: 13. Roman to Integer
    Link: https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        prev = None
        for i in s[::-1]:
            if prev and sym_val[prev]>sym_val[i]:
                num -= sym_val[i]
            else:
                num += sym_val[i]
            prev = i
        return num
