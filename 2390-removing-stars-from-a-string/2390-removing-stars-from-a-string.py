class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        print(s)
        stack = []
        count=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='*':
                count = count+1
            else:
                if count>0:
                    count = count-1
                    continue
                elif count==0:
                    stack.append(s[i])
                    continue
        return "".join(list(reversed(stack)))