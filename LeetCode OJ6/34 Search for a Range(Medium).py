# -*- coding: utf-8 -*-
class Solution(object):
    def searchRange(self, nums, target):
		def find_start(start,end):
			while nums[start] != target:
				if start + 1 == end:
					return end
				temp = (start+end)/2
				if nums[temp] == target:
					end = temp
				else:
					start = temp
			return start
			
		def find_end(start,end):
			while nums[end] != target:
				if start +1 == end:
					return start
				temp = (start+end)/2
				if nums[temp] == target:
					start = temp
				else:
					end = temp
			return end
		
		start = -1
		end = -1
		if nums[0] > target or nums[-1] < target:
			return [-1,-1]
		len0 = len(nums)
		if nums[0] == target:
			start = 0
		if nums[-1] == target:
			end = len0-1
		if start == -1 and end != -1:
			start = find_start(0,len0-1)
		elif start != -1 and end == -1:
			end = find_end(0,len0-1)
		else:
			start0 = 0
			end0 = len0-1
			while 1:
				if end0 - start0 <= 1:
					break
				temp = (start0+end0)/2
				if nums[temp] == target:
					start = find_start(start0,temp)
					end = find_end(temp,end0)
					break
				elif nums[temp] > target:
					end0 = temp
				else:
					start0 = temp
		ans = []
		ans.append(start)
		ans.append(end)
		return ans
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			