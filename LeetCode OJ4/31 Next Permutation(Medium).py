# -*- coding: utf-8 -*-
class Solution(object):
    def nextPermutation(self, nums):
		len0 = len(nums)
		for i in range(len0):
			if len0-i-2 < 0:
				nums.reverse()
				break
			if nums[len0-1-i] > nums[len0-i-2]:
				min0 = 10000000
				index = 0
				for j in range(i+1):
					if nums[len0-1-j] > nums[len0-i-2] and nums[len0-1-j] < min0:
						min0 = nums[len0-1-j]
						index = len0-1-j
				temp = nums[index]
				nums[index] = nums[len0-i-2]
				nums[len0-i-2] = temp
				a = nums[len0-1-i:]
				a.reverse()
				nums[len0-1-i:] = a
				break
				