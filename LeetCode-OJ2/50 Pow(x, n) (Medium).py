# -*- coding: utf-8 -*-
class Solution(object):
    def myPow(self, x, n):
		result = x
		i = 1
		base = 1
		flag = 0   #用来检测n的正负，负数取倒数
		base_num = x
		if n > 0:
			flag = 1
		elif n < 0:
			flag = 0
			n = -n
		else:
			return 1
		while i < n:
			if i + base < n:  #一个加速过程，没有会超时。也可以转化成二进制数，让对应位乘积乘起来，由于是指数，两种算法速度差别不大
				result *= base_num
				i += base
				base_num *= base_num
				base = base*2
			else:
				base = 1
				base_num = x
				result = result*x
				i += 1
		if flag == 1:
			return result
		else:
			return 1/result