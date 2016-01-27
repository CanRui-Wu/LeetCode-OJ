# -*- coding: utf-8 -*-
class Solution(object):
	def isValid(self, s):
		stack = []   #用列表来模拟栈的功能
		ans = {'{':'}','(':')','[':']'}  #建立字典来匹配
		for i in s:
			if i == '{' or i == '[' or i == '(':
				stack.append(i)
			elif i == '}' or i == ']' or i == ')':
				if len(stack) == 0:
					return False
				x = stack.pop()
				if(ans[x] != i)
					return False
			else:   #默认只能输入括号
				return False
		if len(stack) == 0:
			return True
		else:
			return False
        