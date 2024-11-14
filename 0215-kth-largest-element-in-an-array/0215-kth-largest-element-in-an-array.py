class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return list(reversed(sorted(nums)))[k-1]