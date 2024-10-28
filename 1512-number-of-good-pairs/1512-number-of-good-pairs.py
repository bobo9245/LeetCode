import numpy as np
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        arr=[]
        for num in np.unique(nums):
            arr.append(nums.count(num))
        for i in arr:
            if i>1:
                ans = ans+(i*(i-1)/2)
        return int(ans)