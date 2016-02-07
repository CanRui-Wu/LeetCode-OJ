# -*- coding: utf-8 -*-
class Solution(object):
    def search(self, nums, target):
		def binary_serach(start,end):
			if nums[start] == target or nums[end] == target:
				return True
			while 1:
				if end - start <= 1:
					if nums[start] == target or nums[end] == target:
						return True
					else:
						return False
				temp = (start+end)/2
				if nums[temp] == target:
					return True
				elif nums[temp] > target:
					end = temp
				else:
					start = temp

		len0 = len(nums)
		if len0 == 1:
			if nums[0] == target:
				return True
			else:
				return False
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
			elif nums[temp] < nums[end]:
				end = temp
			else:
				if nums[start+1] == nums[start]:
					start +=1
				elif nums[end-1] == nums[end]:
					end -= 1
		if target > nums[-1]:
			return binary_serach(0,rotate)
		else:
			return binary_serach(rotate+1,len0-1) 
