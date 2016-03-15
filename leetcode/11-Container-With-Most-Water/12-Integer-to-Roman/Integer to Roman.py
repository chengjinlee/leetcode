#coding-Utf8
#罗马字符表示
#I = 1;V = 5;X = 10;L = 50;C = 100;D = 500;M = 1000;
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str =''
        i = 0
        symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]    
        value = [1000,900,500,400, 100, 90,  50, 40,  10, 9,   5,  4,   1]   
        while num!=0:  
            while num >= value[i]: 
                num -= value[i]  
                str += symbol[i]
            i +=1
        return str
