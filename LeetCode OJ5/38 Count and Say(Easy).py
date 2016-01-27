# -*- coding: utf-8 -*-
class Solution(object):
	def generate_next(self,current):
		len0 = len(current)
		result = []
		number = 1
		if len0 == 1:
			result.append(str(1))
			result.append(str(current[len0-1]))
			return ''.join(result)
		for i in range(1,len0):
			if current[i] == current[i-1]:
				number += 1
			else:
				result.append(str(number))
				result.append(str(current[i-1]))
				number = 1
			if i == len0-1:
				result.append(str(number))
				result.append(str(current[i]))
		return ''.join(result)
				
	def countAndSay(self, n):
		current = "1"
		if n == 1:
			return current
		for i in range(n-1):
			current = self.generate_next(current)
		return current
