# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
		def backtrack(ans,current_ans,candidates,target):
			len0 = len(candidates)
			for i in range(len0):
				value = candidates[i]
				current_ans.append(value)
				if value < target:
					backtrack(ans,current_ans,candidates[i+1:],target-value)
					current_ans.pop()
				elif value == target:
					if current_ans not in ans:
						ans.append(current_ans[:])
					current_ans.pop()
					return
				else:
					current_ans.pop()
			return
		
		ans = []
		current_ans = []
		temp = candidates[:]
		temp.sort()
		backtrack(ans,current_ans,temp,target)
		return ans