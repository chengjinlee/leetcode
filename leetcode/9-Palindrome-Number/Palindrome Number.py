class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        answer = 0
        a=abs(x)
        while a > 0:
            answer = answer*10 + a%10
            a = a/10
        if answer == x:
            return True
        else:
            return False
