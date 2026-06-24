class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1                       # 1이 이미 첫 번째 (전위 순회의 시작점)
        while k > 0:
            steps = self.count(curr, n)
            if steps <= k:           # k번째가 curr 서브트리 밖 → 옆으로
                curr += 1
                k -= steps
            else:                    # k번째가 curr 서브트리 안 → 아래로
                curr *= 10
                k -= 1
        return curr

    def count(self, prefix: int, n: int) -> int:
        steps = 0
        first = last = prefix
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps