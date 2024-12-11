class Solution:
    def reverse(self, x: int) -> int:
        isneg=True if x<0 else False
        if str(x)=='0':
            return 0
        s=int(str(x).lstrip('-')[::-1].lstrip('0'))
        print(s)
        s= -s if isneg else s
        if s<-(2**31) or s>2**31-1:
            return 0
        return s