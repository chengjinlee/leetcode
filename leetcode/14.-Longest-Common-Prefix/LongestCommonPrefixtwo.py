#!/usr/bin/python
#_*_ coding:utf-8 _*_

class Solution(object):  
    def longestCommonPrefix(self, strs):  
        """ 
        :type strs: List[str] 
        :rtype: str 
        """
        strNum=len(strs)  #字符串的长度
        if strNum == 0 or strs == None:
            return ''
        else:
            prefix = strs[0]        #对前缀进行赋值
            for i in range(strNum):
                if prefix == '' or strs[i] == '':
                    return ''
                comlen = min(len(prefix),len(strs[i]))  #减少寻找公共最小前缀的长度
                j = 0
                while j < comlen and prefix[j] == strs[i][j]:  #寻找寻找公共最小前缀
                    j += 1
                prefix = prefix[0:j]
        return prefix
