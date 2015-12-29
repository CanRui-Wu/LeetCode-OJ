# -*- coding: utf-8 -*-
import copy
class Solution(object):
	def __init__ (self):
		self.end1 = 0
		self.end2 = 0
		self.b = []
		a = [None]*104
		for i in range(104):
			c = copy.deepcopy(a)
			self.b.append(c)
	def uniquePathsWithObstacles(self, obstacleGrid):
		self.end1 = len(obstacleGrid)-1
		self.end2 = len(obstacleGrid[0])-1
		return self.get_ans(0,0,obstacleGrid)
	def get_ans(self,start1,start2,obstacleGrid):
		if start1 > self.end1 or start2 > self.end2:
			return 0
		if obstacleGrid[start1][start2] == 1:
			return 0
		if self.b[start1][start2] != None:
			return self.b[start1][start2] 
		if start1 == self.end1 and start2 == self.end2:
			return 1
		self.b[start1][start2] = self.get_ans(start1+1,start2,obstacleGrid)+self.get_ans(start1,start2+1,obstacleGrid)
		return self.b[start1][start2]
