# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
		def backtrack(ans,current_ans,candidates,target):
			len0 = len(candidates)
			for i in range(len0):
				value = candidates[i]
				current_ans.append(value)
				if value < target:
					backtrack(ans,current_ans,candidates[i:],target-value)
					current_ans.pop()
				elif value == target:
					ans.append(current_ans[:])   #不能简单的放current_ans
					current_ans.pop()
					return
				else:
					current_ans.pop()
			return
		
		ans = []
		current_ans = []
		temp = candidates[:]   #取无关副本进行排序
		temp.sort()               
		backtrack(ans,current_ans,temp,target)
		return ans