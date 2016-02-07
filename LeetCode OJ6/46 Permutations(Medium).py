# -*- coding: utf-8 -*-
class Solution(object):
    def permute(self, nums):
		ans = []
		current = []
		len0 = len(nums)
		def choose():
			if len(current) == len0:
				temp = []
				for i in current:
					temp.append(nums[i])
				ans.append(temp)
				return
			for i in range(len0):
				if i not in current:
					current.append(i)
					choose()
					current.pop()
		choose()
		return ans