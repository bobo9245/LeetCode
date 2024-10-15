class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps=0
        zeros=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='1':
                swaps+=zeros
            else:
                zeros=zeros+1
        return swaps
                