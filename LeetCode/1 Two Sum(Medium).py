# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
		length = len(nums)
		for i in range(length):	#遍历寻找，设置j比i大	
			for j in range(i+1,length):
				if nums[i]+nums[j] == target: #每两个尝试加起来与目标数值对比
					ans = []
					ans.append(i+1)
					ans.append(j+1)
					return ans