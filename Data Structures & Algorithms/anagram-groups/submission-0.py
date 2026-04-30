class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            fingerprint = "".join(sorted(word))  # "eat" → "aet"
            groups.setdefault(fingerprint, []).append(word) #setDefaults  
        return list(groups.values()) 