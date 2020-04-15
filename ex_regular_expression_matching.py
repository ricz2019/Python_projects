# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

import re

# def isMatch(s,p):
# 	"""type s:str
# 	type p: str
# 	rtpye: bool
# 	"""
# 	state = 0
def isMatch(text, pattern):
	# dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

	# dp[-1][-1] = True
	# print(dp)
	# for i in range(len(text), -1, -1):
	# 	for j in range(len(pattern) - 1, -1, -1):
	# 		first_match = i < len(text) and pattern[j] in {text[i], '.'}
	# 		if j+1 < len(pattern) and pattern[j+1] == '*':
	# 			dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
	# 			print(dp[i][j], 'i = ', i, ' j= ', j)
	# 		else:
	# 			dp[i][j] = first_match and dp[i+1][j+1]

	# print(dp)	
	# return dp[0][0]
	i, j = len(s)-1, len(p)-1

	while i >= 0 and j >= 0:
		if p[j] == s[i]:
			i, j = i - 1, j - 1
		
		else:
			if p[j] == '.':
				i, j = i - 1, j - 1
			elif p[j] == '*':
				print(p[j])
				if j == 0:
					return False
			
				if p[j-1] == s[i-1]:
					if p[j-1] == s[i]:
						i -= 1
					else:
						j -= 1
				elif p[j-1] == '.':
					
					if j-2 >= 0:
						if p[j-2] == s[i]:
							print('i,j', i,j, p[:j-2], s[i])
							j = j -2
					i -= 1
				else:
					j -= 1
			else:
				return False
			
	return True			

s = 'abaaaaaaabcd'
p = 'ab.*bcd'

print(isMatch(s,p))

# list = ["guru99 get", "guru99 give", "guru Selenium"]

# for element in list:
# 	print(element)
# 	z = re.match(r"^g\w+\sg\w+", element)
# 	if z:
#     # print('result = ', (z.groups()))
# 		print('result = ', z.groups())
    
# patterns = ['software testing', 'guru99']
# text = 'software testing is fun?'
# for pattern in patterns:
#     print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
#     if re.search(pattern, text):
#         print('found a match!')
# else:
#     print('no match')
# abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
# emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
# for email in emails:
#     print(email)