from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    nums_set = set()
    for num in nums:
        nums_set.add(num)
    return False if len(nums_set) == len(nums) else True
