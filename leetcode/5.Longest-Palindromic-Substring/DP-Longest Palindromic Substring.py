#codeing utf-8
class Solution(object):
    def longest_common_subsequence(self,s):
        lens = len(s)
        if lens <= 1 :
            return s
        sleft,sright = 0,0
        dp=[[0 for i in range(lens)] for j in range(lens)]
        for i in range(1,lens):
            dp[i][i] = True
            dp[i][i-1] = True
        for i in range(2,lens):
            for j in range(0,lens-i):
                if s[j] == s[j+i-1] and dp[j+1][j+i-2] :
                    dp[j][j+i-1] = True
                    if sright-sleft+1 < i:
                        sleft = j
                        sright = j+i-1
        return s[sleft:sright-sleft+1]               
                
a=Solution()
print (a.longest_common_subsequence('abccbaaa'))
