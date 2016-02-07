# -*- coding: utf-8 -*-
class Solution(object):
    def searchInsert(self, nums, target):
		len0 = len(nums)
		if nums[0] > target:
			return 0
		if nums[-1] < target:
			return len0
		start = 0
		end = len0-1
		while 1:
			if end - start <= 1:
				if nums[start] == target:
					return start
				else:
					return end
			temp = (start+end)/2
			if nums[temp] == target:
				return temp
			elif nums[temp] > target:
				end = temp
			else:
				start = temp