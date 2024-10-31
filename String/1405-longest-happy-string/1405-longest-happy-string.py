class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result, curra, currb, currc = [], 0, 0, 0
        for _ in range(a + b + c):
            if (a >= b and a >= c and curra != 2) or (a > 0 and (currb == 2 or currc == 2)):
                result.append("a")
                a, curra, currb, currc = a - 1, curra + 1, 0, 0
            elif (b >= a and b >= c and currb != 2) or (b > 0 and (curra == 2 or currc == 2)):
                result.append("b")
                b, currb, curra, currc = b - 1, currb + 1, 0, 0
            elif (c >= a and c >= b and currc != 2) or (c > 0 and (curra == 2 or currb == 2)):
                result.append("c")
                c, currc, curra, currb = c - 1, currc + 1, 0, 0
        return "".join(result)
