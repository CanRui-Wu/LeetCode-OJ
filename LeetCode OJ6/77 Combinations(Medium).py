# -*- coding: utf-8 -*-
class Solution(object):
    def combine(self, n, k):
		current = []
		ans = []
		def choose():
			len0 = len(current)
			if  len0 == k:
				temp = current[:]
				ans.append(temp)
				return
			for i in range(1,n+1):
				if i not in current and (len0 == 0 or i > current[len0-1]):
					current.append(i)
					choose()
					current.pop()
		choose()
		return ans