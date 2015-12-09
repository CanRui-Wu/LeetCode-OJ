# -*- coding: utf-8 -*-
class Solution(object):
    def addTwoNumbers(self, l1, l2):
		temp = ListNode(2)
		ans = temp
		temp1 = l1
		temp2 = l2
		end_of_l1 = 0  #判断l1是否结束，先结束在后面运算中全为0
		end_of_l2 = 0  #判断l2是否结束，先结束在后面运算中全为0
		add1 = 0  #每次做加法的第一个数
		add2 = 0  #每次做加法的第二个数
		carry = 0 #做加法时产生的进位
		cal = 0   #做加法计算出的结果
		while 1:
			if end_of_l1 == 1:
				add1 = 0
			elif temp1.next == None:
				add1 = temp1.val
				end_of_l1 = 1
			else:
				add1 = temp1.val
			if end_of_l2 == 1:
				add2 = 0
			elif temp2.next == None:
				add2 = temp2.val
				end_of_l2 = 1
			else:
				add2 = temp2.val
			if	add1+add2+carry < 10:
				cal = add1+add2+carry
				carry = 0
			else:
				cal = add1+add2+carry-10
				carry = 1
			temp.val = cal
			if end_of_l1 and end_of_l2:  #两个都结束时，程序结束，有进位就补一个1
				if carry == 0:
					break
				else:
					temp.next = ListNode(1)
					break
			if end_of_l1 == 0:
				temp1 = temp1.next
			if end_of_l2 == 0:
				temp2 = temp2.next
			temp3 = ListNode(0)  
			temp.next = temp3
			temp = temp.next
		return ans