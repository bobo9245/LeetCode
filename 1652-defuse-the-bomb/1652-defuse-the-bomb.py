class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(code)):
            s=0
            if k==0:
                ans.append(0)
            else:
                if k>0:
                    for j in range(1,k+1,1):
                        s = s + code[(i+j)%len(code)]
                elif k<0:
                    for j in range(-1,k-1,-1):
                        s = s+code[(i+j)%len(code)]
                ans.append(s)
        print(ans)
        return(ans)