# -*- coding: utf-8 -*-
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		if s == "" :   #空字符直接返回
			return 0
		dp = []        #采用动态规划处理，dp[i]表示以i结尾最长的子串长度
		len0 = len(s) 
		dp.append(1)
		start = 0
		ok = 1
		result = 1
		for i in range(1,len0):      #如果与上一个最长子串相比没有任何相同的，则+1，否则从相同的后面一个作为i结尾最长串的起点
			for j in range(start,i):
				if s[i] != s[j]:         
					continue
				else:
					ok = 0
					dp.append(i-j)
					start = j+1
					break
			if ok == 1:
				dp.append(dp[i-1]+1)
			ok = 1
			if dp[i] > result:
				result = dp[i]										
		return result

