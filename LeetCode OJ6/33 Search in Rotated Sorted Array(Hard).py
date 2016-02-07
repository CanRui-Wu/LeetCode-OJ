# -*- coding: utf-8 -*-
class Solution(object):
    def search(self, nums, target):
		def binary_serach(start,end):
			if nums[start] == target:
				return start
			elif nums[end] == target:
				return end
			while 1:
				if end - start <= 1:
					if nums[start] == target:
						return start
					elif nums[end] == target:
						return end
					else:
						return -1
				temp = (start+end)/2
				if nums[temp] == target:
					return temp
				elif nums[temp] > target:
					end = temp
				else:
					start = temp

		len0 = len(nums)
		if len0 == 1:
			if nums[0] == target:
				return 0
			else:
				return -1
		if nums[0] < nums[-1]:
			return binary_serach(0,len0-1)
		start = 0
		end = len0-1
		rotate = -1
		while 1:
			if end - start == 1:
				rotate = start
				break
			temp = (start+end)/2
			if nums[temp] > nums[end]:
				start = temp
			else:
				end = temp
		if target > nums[-1]:
			return binary_serach(0,rotate)
		else:
			return binary_serach(rotate+1,len0-1)