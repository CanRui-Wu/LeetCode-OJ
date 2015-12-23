# -*- coding: utf-8 -*-
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
		temp = head       #temp作为head的一个引用
		num_node = 0      #记录链表中结点个数
		while temp != None:
			num_node += 1
			temp = temp.next
		num_group = num_node/k   #记录可以被k分成的组数
		ans = ListNode(0)        #建立答案头指针，结尾返回ans
		ans_temp = ans           #建立一个部分答案
		temp = head		  #temp遍历过已经改变，重新赋值为head的引用
		for i in range(num_group):
			for j in range(k):
				if j == 0:
					first = temp
				cur = temp.next
				temp.next = ans_temp.next
				ans_temp.next = temp
				temp = cur
			ans_temp = first
		ans_temp.next = temp
		return ans.next