from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = defaultdict(int)
        for i in range(0, len(nums)):
            if target-nums[i] in n:
                return [n[target-nums[i]], i]
            n[nums[i]] = i

        