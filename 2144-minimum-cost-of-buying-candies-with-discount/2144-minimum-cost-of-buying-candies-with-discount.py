class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        c = list(reversed(sorted(cost)))
        print(c)
        tot = 0
        for i in range(0,len(c)):
            if i%3==2:
                pass
            else:
                tot = tot+c[i]
        return tot