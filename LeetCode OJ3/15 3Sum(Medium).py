# -*- coding: utf-8 -*-
import copy
class Solution(object):
    def threeSum(self, nums):
		num_ans = 0
		ans = []
		len0 = len(nums)
		temp = copy.deepcopy(nums)  #深拷贝，以免影响传入的列表
		temp.sort()
		for i in range(len0):
			if i > 0 and temp[i] == temp[i-1]:  #去重
				continue
			j = i+1     #头尾指针往中间靠拢
			k = len0-1
			a = temp[i]
			while j < k:
				b = temp[j]
				c = temp[k]
				temp_ans = []
				temp_ans.append(a)
				temp_ans.append(b)
				temp_ans.append(c)
				if a+b+c == 0:
					if num_ans == 0:
						ans.append(temp_ans)
						num_ans += 1
					elif temp_ans != ans[num_ans-1]:
						ans.append(temp_ans)
						num_ans += 1
					j += 1
					k -= 1
				elif a+b+c < 0:
					j += 1
				else:
					k -=1
		return ans