# -*- coding: utf-8 -*-
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		ans = ListNode(0) #建立答案头指针
		ans_temp = ans
		while 1:
			if l1 == None and l2 == None:
				break
			if l1 == None:
				ans_temp.next = l2
				l2 = l2.next
			elif l2 == None:
				ans_temp.next = l1
				l1 = l1.next
			elif l1.val < l2.val:
				ans_temp.next = l1
				l1 = l1.next
			else:
				ans_temp.next = l2
				l2 = l2.next
			ans_temp = ans_temp.next
		return ans.next