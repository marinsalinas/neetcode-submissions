class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1 #formula to learn 
            groups[tuple(count)].append(word) #setDefaults  
        return list(groups.values()) 