# -*- coding: utf-8 -*-
class Solution(object):
    def permuteUnique(self, nums):
		unique = []
		times = []
		for i in nums:
			if i not in unique:
				unique.append(i)
				times.append(1)
			else:
				times[unique.index(i)] += 1
		ans = []
		current = []
		len0 = len(nums)
		len1 = len(unique)
		def choose():
			if len(current) == len0:
				temp = []
				for i in current:
					temp.append(unique[i])
				ans.append(temp)
				return
			for i in range(len1):
				if times[i] != 0:
					times[i] -= 1
					current.append(i)
					choose()
					current.pop()
					times[i] += 1
		choose()
		return ans	