# -*- coding: utf-8 -*-
class Solution(object):
    def mySqrt(self, x):
		a = 0
		b = x
		while 1:
			temp = (a+b)/2
			if temp*temp == x:
				return temp
			elif temp*temp > x:
				b = (a+b)/2
			else:
				a = (a+b)/2
			if b-a == 1:
				if b*b == x:
					return b
				else:
					return a