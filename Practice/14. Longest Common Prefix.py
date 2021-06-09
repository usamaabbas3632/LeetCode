'''
Task Details
    Platform: LeetCode
    Name: 14. Longest Common Prefix
    Link: https://leetcode.com/problems/longest-common-prefix/
'''

class Solution:
    
    def find_min_len(self, strs):
        min_len = 10000
        for s in strs:
            if min_len > len(s):
                min_len = len(s)
        return min_len
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if not strs:
            return lcp
        pre_ind = 1
        iterations = self.find_min_len(strs)
        while iterations:
            pre = strs[0][:pre_ind]
            for s in strs:
                if not s.startswith(pre) :
                    return lcp                    
            lcp = pre
            pre_ind += 1
            iterations -= 1
        return lcp