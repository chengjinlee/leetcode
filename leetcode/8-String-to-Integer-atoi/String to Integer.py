#利用正则表达式

 Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        stri=str.strip()
        stri=re.findall('(^[\+\-0]*\d+)\D*',stri)
        try:
            result = int(''.join(stri))
            MaxInt = 2147483647
            MinInt = -2147483648
            if result > MaxInt >0 :
                return MaxInt
            elif result < MinInt <0:
                return MinInt
            else:
                return result
                    
        except:
            return 0
