# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):  #最长回文子串,用manacher算法
		len0 = len(s)
		l = list(s)     #为了对字符串进行预处理，转成列表，添加n+1个#在字符旁，使得总数为2n+1奇数
		for i in range(len0):
			l.insert(2*i,'#')
		l.insert(2*len0,'#')
		len0 = 2*len0+1
		p = []      #p[i]放的是以i为中心能扩张的程度，如l[i] = b,那么 #a#c#b#c#d#的p[i]为4,故字符#的p[i]必定奇数，原字符必定偶数
		mx = 1
		id = 0
		for i in range(len0):   
			if mx > i and 2*id-i >= 0 and 2*id-i < len(p): 
				if(p[2*id-i] > mx - i): #manacher算法关键，符合条件的可以从前面的p[i]获得下界，从较高的值开始尝试匹配
					p.append(mx-i)   
				else:					#不符合条件的值智能从旁边开始匹配
					p.append(p[2*id-i])
			else:
				p.append(1)
			while 1:          #不断扩张，直到两边字符不匹配          
				if i+p[i] >= len0 or i-p[i] <= -1:
					break
				if l[i+p[i]] == l[i-p[i]]:
					p[i] += 1
				else:
					break
			if mx < i+p[i]:
				id = i
				mx = i+p[i]
		max = 1
		index = 0
		for i in range(len0):
			if p[i] > max:
				max = p[i]
				index = i
		start = -1
		length = -1
		length = p[index]-1
		if index%2 == 0:   #对#号和原始字符分别处理
			start = index/2 - length/2
		else:
			start = (index-1)/2 - (length-1)/2
		return s[start:start+length]
