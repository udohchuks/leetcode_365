"""
Question:
Given an integer array nums, return true if any 
value appears more than once in the array, otherwise return false.

Logic: The hash datastrcuture allows for unique entry and quick retrieval
"""
from types import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = {}
        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                return True
        return False