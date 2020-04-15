# Python: search longest palindromes within 
# a word and palindromes within a word/string
# s3 = 'acsdfvgbhnjggggggggggggggggggggggggggggg'	

# def palindromes(text):
# 	text = text.lower()
# 	results = ''

# 	for i in range(len(text)):
# 		for j in range(0, i+1):
# 			chunk = text[j : i+1]
# 			if chunk == chunk[::-1]:
# 				if len(chunk) > len(results):
# 				# results.append(chunk)
# 					results = chunk

# # 	return results	

# print('palindromes', palindromes(s3))


class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		results = ''

		for i in range(len(s)-1, -1, -1):
			if len(results) > i:
				break

			for j in range(0, i+1):

				chunk = s[j : i+1]
				if chunk == chunk[::-1]:
					if len(chunk) > len(results):
						results = chunk
				if len(results) > (i - j):
					break


		return results

    
def main():
    test_obj = Solution()
    test = 'a'
    test = "111112321111234567898765432111111"
    print('test string is ',test,len(test))
    ret = test_obj.longestPalindrome(test)
    print(test_obj.longestPalindrome(test), len(ret))

if __name__ == '__main__':
    main()