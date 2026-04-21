class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for x in s:
            count_s[x] = count_s.get(x, 0) + 1

        for j in t:
            count_t[j] = count_t.get(j, 0) + 1


        for k in count_s.keys():
            if count_s[k] != count_t.get(k, 0):
                return False
        return True
            