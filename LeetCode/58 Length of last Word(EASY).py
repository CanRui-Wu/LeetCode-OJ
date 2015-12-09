class Solution(object):
    def lengthOfLastWord(self, s):
		length = len(s);
		num = 0
		for i in range(length):
			if s[length-1-i] != " ":
				num += 1
			elif num != 0:
				break
		return num