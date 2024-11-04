class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list1 = list(word1)
        list2 = list(word2)
        ans = []
        for i in range(max(len(word1),len(word2))):
            if i<len(list1):
                ans.append(list1[i])
            if i<len(list2):
                ans.append(list2[i])
        return ''.join(ans)