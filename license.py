class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        #remove hyphens
        nonHyphenStr = S.replace("-","")
        strLen = len(nonHyphenStr)
        firstGroupLen = strLen % K

        newStr = ''
    	while firstGroupLen > 0:
    		if firstGroupLen == 1:
    			newStr = newStr + nonHyphenStr[0] + '-'
    			nonHyphenStr = nonHyphenStr[1:]
    		else:
	    		#add new char
	    		newStr = newStr + nonHyphenStr[0]
	    		#remove the char from nonHyphenStr
	    		nonHyphenStr = nonHyphenStr[1:]
    		firstGroupLen -= 1
        #loop through string placing a hyphen every K spots
        for idx, char in enumerate(nonHyphenStr):
        	if idx % K == 0 and idx != 0:
        		newStr = newStr + '-'+char
        	else:
        		newStr = newStr + char

        return newStr.upper()



sol = Solution()
print sol.licenseKeyFormatting("2-4A0r7-4k", 4)
print sol.licenseKeyFormatting("2-4A0r7-4k", 3)