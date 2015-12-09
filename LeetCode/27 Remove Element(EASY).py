# -*- coding: utf-8 -*-
class Solution(object):
    def removeElement(self, nums, val):
		temp = list(nums) #原数组需要删除，避免复杂化先存个副本
		init_len = len(nums)
		num_val = 0 #记录有多少个需要删除的
		for i in range(init_len):
			if temp[i] == val:
				del(nums[i-num_val])
				num_val += 1
		return init_len-num_val
