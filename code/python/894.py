# https://leetcode.com/problems/all-possible-full-binary-trees/
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: return []
        if n == 1: return [TreeNode()]
        res = []
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)
            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)
        return res
