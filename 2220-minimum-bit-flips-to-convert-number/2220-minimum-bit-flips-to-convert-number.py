def count_differences(str1, str2):
    # 두 문자열의 길이를 맞추기 위해 짧은 쪽을 0으로 채웁니다.
    max_len = max(len(str1), len(str2))
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)

    # 두 문자열을 비교하여 다른 글자의 개수를 셉니다.
    difference_count = sum(c1 != c2 for c1, c2 in zip(str1, str2))

    return difference_count


def pad_strings(str1, str2):
    # 두 문자열의 최대 길이를 구합니다.
    max_len = max(len(str1), len(str2))

    # 두 문자열을 최대 길이에 맞춰 0으로 채웁니다.
    str1 = str1.zfill(max_len)
    str2 = str2.zfill(max_len)

    return str1, str2


class Solution:

    def minBitFlips(self, start: int, goal: int) -> int:
        s = format(start, "b")
        g = format(goal, "b")
        s, g = pad_strings(s, g)
        n = count_differences(s, g)
        print(n)
        return n
