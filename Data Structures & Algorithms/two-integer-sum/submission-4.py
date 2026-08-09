from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i in range(0, len(nums)):
            if (target - nums[i]) in d:
                print(i, nums[i], target-nums[i], d[target-nums[i]])
                return [d[target - nums[i]], i]
            if nums[i] not in d:
                d[nums[i]] = i
        