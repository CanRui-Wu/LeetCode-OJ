# -*- coding: utf-8 -*-
import copy
class Solution(object):
	def __init__ (self):
		self.b = []
		a = [None]*104
		for i in range(104):
			c = copy.deepcopy(a)
			self.b.append(c)
	def uniquePaths(self, m, n):
		if self.b[m][n] != None:
			return self.b[m][n]
		if m == 1 or n == 1:
			return 1
		self.b[m][n] = self.uniquePaths(m,n-1)+self.uniquePaths(m-1,n)
		return self.b[m][n]
