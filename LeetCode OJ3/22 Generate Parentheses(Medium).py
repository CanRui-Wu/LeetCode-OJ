# -*- coding: utf-8 -*-
class Solution(object):
	def _init_(self):  #初始化类
		self.n = 0
	def find_ans(self,ans,index1,index2,temp): #递归调用此函数找答案加入到ans中
		if index1+index2 == 2*self.n:
			one_of_ans = ''.join(temp)
			ans.append(one_of_ans)
			return
		if index1 < self.n:
			temp.append('(')
			self.find_ans(ans,index1+1,index2,temp)
			temp.pop()
		if index1 > index2:
			temp.append(')')
			self.find_ans(ans,index1,index2+1,temp)
			temp.pop()
	def generateParenthesis(self, n):  #temp用来存储一个当前的答案，ans用来存放正确的答案
		self.n = n
		temp = []
		ans = []
		self.find_ans(ans,0,0,temp)
		return ans
	
	