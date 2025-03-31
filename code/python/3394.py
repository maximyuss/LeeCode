# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(dim) -> bool:
            rectangles.sort(key=lambda x: x[dim])
            cnt = 0
            max_end = 0
            for r in rectangles:
                if max_end <= r[dim]:
                    cnt += 1
                    if cnt == 3:
                        return True
                if max_end < r[dim + 2]:
                    max_end = r[dim + 2]
            return False

        return check(0) or check(1)
