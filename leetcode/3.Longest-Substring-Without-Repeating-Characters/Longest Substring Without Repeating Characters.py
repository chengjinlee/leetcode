#Codeing-Utf8
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0          #记录子字符串的起点
        maxlen =           #记录最长子字符串的长度
        dict = {}          #用字典记录所有不重复的字符
        for i in range(len(s)):  #进行赋值 
            dict[s[i]] = -1
        for i in range(len(s)):
            if dict[s[i]] != -1:    #存在重复的字符
                while start <= dict[s[i]]:  #利用循环记录重复字符的个数
                    dict[s[start]] = -1     #将重复的字符之前的字符的标记都置为-1
                    start += 1
            if i - start + 1 > maxlen: maxlen = i - start + 1
            dict[s[i]] = i
        return maxlen
