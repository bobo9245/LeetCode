class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1] + n)

        return max(preSum) - min(preSum)