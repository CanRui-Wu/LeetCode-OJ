# -*- coding: utf-8 -*-
class Solution(object):
    def threeSumClosest(self, nums, target):
		len0 = len(nums)
		flag = 0  #flag用来标记目前最近的值是小于target还是大于target
		dis = 0   #用来计算目前最近的与target相差的绝对值
		nums.sort()
		if nums[0]+nums[1]+nums[2]-target > 0:
			flag = 1
			dis = nums[0]+nums[1]+nums[2]-target
		elif nums[0]+nums[1]+nums[2]-target < 0:
			flag = 0
			dis = target-nums[0]-nums[1]-nums[2]
		else:
			return target		
		for i in range(len0):   #固定一位，然后剩余两位指向头尾指针，向中间收缩复杂度O(n*n)
			j = i+1
			k = len0-1
			while j < k:
				temp = nums[i]+nums[j]+nums[k]
				if temp == target:
					return target
				elif temp > target:
					if temp-target < dis:
						flag = 1
						dis = temp-target
					k -= 1
				else:
					if target-temp < dis:
						flag = 0
						dis = target-temp
					j += 1
		if flag == 1:
			return target+dis
		else:
			return target-dis
							
					