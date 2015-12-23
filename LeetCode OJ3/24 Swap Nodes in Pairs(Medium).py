# -*- coding: utf-8 -*-
#对象间的赋值相当于引用，除非改变的是整个对象，否则他们应该一致
#如a = b,那么a.append(0),b会改变，但是a = c,那么a与b之间就无关系了
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
    def swapPairs(self, head):
		if head == None or head.next == None:
			return head
		temp = ListNode(0)
		temp.next = head
		a = temp
		b = a.next
		c = b.next
		d = c.next
		while 1:
			a.next = c
			c.next = b
			b.next = d
			a = a.next
			a = a.next
			b = a.next
			if b == None:
				break
			c = b.next
			if c == None:
				break
			d = c.next
		return temp.next