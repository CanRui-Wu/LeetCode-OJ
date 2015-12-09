# -*- coding: utf-8 -*-
class Solution(object):
    def plusOne(self, digits):
		length = len(digits)
		ans_list = list(digits)
		ok = 0  #判断是否全为9，全为9的情况需要加一位
		for i in range(length):
			temp = ans_list[length-1-i]
			if temp != 9:
				ans_list[length-1-i] += 1
				ok = 1
				break
			else:
				ans_list[length-1-i] = 0
		if ok == 0:
			ans_list.insert(0,1)
		return ans_list