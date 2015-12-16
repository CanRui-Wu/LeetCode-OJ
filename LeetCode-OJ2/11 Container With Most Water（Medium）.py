# -*- coding: utf-8 -*-
class Solution(object):
	def	Area(self,x,y,z): #一个简单的计算面积的函数
		if x > y:
			return y*z
		else:
			return x*z
	def maxArea(self, height):  #贪心算法，时间复杂度o(n)
		len0 = len(height)
		pointer1 = 0
		pointer2 = len0-1
		water_max = self.Area(height[0],height[len0-1],len0-1) 
		while pointer1 < pointer2:  
			if self.Area(height[pointer1],height[pointer2],pointer2-pointer1) > water_max:
				water_max = self.Area(height[pointer1],height[pointer2],pointer2-pointer1)
			if height[pointer1] > height[pointer2]:
				pointer2 -= 1
			else:
				pointer1 += 1
		return water_max
	

thing =	Solution()
height = [1,3,5,6,7,4,5,3,8,4]
print thing.maxArea(height)