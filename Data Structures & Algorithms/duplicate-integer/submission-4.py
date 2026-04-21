class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #First shot
        counter = {}
        for x in nums:
            counter[x] = counter.get(x, 0) + 1
            if counter[x] > 1:
                return True
        return False

        #second shot - set is better since we dont need to rely in the
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False