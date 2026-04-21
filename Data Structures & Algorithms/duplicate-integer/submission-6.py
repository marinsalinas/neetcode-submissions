class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #First shot - takes less time more memory
        # counter = {}
        # for x in nums:
        #     counter[x] = counter.get(x, 0) + 1
        #     if counter[x] > 1:
        #         return True
        # return False

        #second shot - takes more time less memory
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False