from collections import deque

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        level_sums = []
        queue = deque([root])

        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(level_sum)

        if len(level_sums) < k:
            return -1
        
        return sorted(level_sums, reverse=True)[k - 1]
