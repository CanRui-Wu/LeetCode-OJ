# -*- coding: utf-8 -*-
import copy
class Solution(object):
	def __init__ (self):
		self.end1 = 0
		self.end2 = 0
		self.b =[]
		
	def minPathSum(self, grid):
		self.b =[[None for i in range(len(grid[0]))] for i in range(len(grid))]
		self.end1 = len(grid)-1
		self.end2 = len(grid[0])-1
		return self.get_ans(0,0,grid)
		
	def get_ans(self,start1,start2,grid):
		if start1 > self.end1 or start2 > self.end2:
			return 99999999999
		if self.b[start1][start2] != None:
			return self.b[start1][start2]
		if start1 == self.end1 and start2 == self.end2:
			return grid[start1][start2]
		self.b[start1][start2] = grid[start1][start2]+min(self.get_ans(start1+1,start2,grid),self.get_ans(start1,start2+1,grid))
		return self.b[start1][start2]