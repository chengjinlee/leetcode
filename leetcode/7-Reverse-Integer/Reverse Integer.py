class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        if x >=0 :
            while x > 0:
                answer = answer*10 + x%10
                x = x/10
            if answer > 2147483647:
                return 0
            else:
                return answer
        else:
            x=abs(x)
            while x > 0:
                answer = answer*10 + x%10 
                x = x/10
            if -answer < -2147483648:
                return 0
            else:
                return -answer
