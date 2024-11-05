class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for c in candies:
            isMax = True if c+extraCandies >= max(candies) else False
            ans.append(isMax)
            
        return ans