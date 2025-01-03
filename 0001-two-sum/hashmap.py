class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}

        for index, value in enumerate(nums):
            diff = target-value
            if diff in HashMap:
                return [HashMap[diff], index]
            HashMap[value] = index
