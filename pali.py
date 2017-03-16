class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        else:
	        numList = [int(n) for n in str(x)]
	        answer = True
	        iters = int(len(str(abs(x)))/2)
	        i = 0
	        j = 1
	        while i < iters:
	        	if numList[i] !=  numList[-j]:
	        		answer = False
	        		break
	        	else:
	        		i += 1
	        		j += 1
	        return answer
sol = Solution()
print sol.isPalindrome(415174)