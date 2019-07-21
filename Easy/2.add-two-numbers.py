#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        output = ListNode(l1.val+l2.val)
        add = int((l1.val+l2.val)/10)
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            output.next =  ListNode((l1.val+l2.val+add)%10)
            output = output.next
            add = (l1.val+l2.val+add)//10
            l1 = l1.next
            l2 = l2.next

        return output

