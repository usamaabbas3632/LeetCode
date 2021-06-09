'''
Task Details
    Platform: LeetCode
    Name: 141. Linked List Cycle
    Link: https://leetcode.com/problems/linked-list-cycle
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            else:
                visited.add(head)
                head = head.next
        return False