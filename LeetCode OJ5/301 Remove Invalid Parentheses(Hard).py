# -*- coding: utf-8 -*-
class Solution(object):		
	def removeInvalidParentheses(self, s):
		def isvalid(s):
			a = 0
			for i in s:
				a += {'(':1,')':-1}.get(i,0)
				if a < 0:
					return False
			if a == 0:
				return True
			else:
				return False
			
		number = -1
		queue = collections.deque([s])
		visit = set([s])
		ans = []
		temp = ""
		while queue:
			x = queue.popleft()
			number = len(x)
			if isvalid(x):
				ans.append(x)
				break
			else:
				ok = 0
				for i in range(number):
					if x[i] == '(' or x[i] == ')':
						ok = 1
						temp = x[:i]+x[i+1:]
						if temp not in visit:
							visit.add(temp)
							queue.append(temp)
				if ok == 0:
					special = x
		for i in queue:
			if isvalid(i):
				ans.append(i)
		return ans
