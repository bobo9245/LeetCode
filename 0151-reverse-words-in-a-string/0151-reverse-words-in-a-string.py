class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(reversed(list(s.strip().split(' '))))
        print(l)
        for n in l:
            n.strip()
        while '' in l:
            l.remove('')
        print(l)
        return " ".join(l)