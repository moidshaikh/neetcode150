from typing import List, Any
from ..utils.testing_helper import assert_solution
import pytest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # contains_duplicate: bool = False
        # nums_set = []
        # for i in range(len(nums)):
        #     if nums[i] in nums_set:
        #         contains_duplicate = True
        #         break
        #     else:
        #         nums_set.append(nums[i])
        # return contains_duplicate
        return len(nums) != len(set(nums))


test_cases: list[tuple[Any, Any]] = [
    ([12, 35, 1, 10, 34, 1], True),
    ([10, 5, 10], True),
    ([10, 10, 10], True),
    ([1,2,3,4], False),
]


@pytest.mark.parametrize("arr, expected", test_cases)
def test_solution(arr, expected):
    sol = Solution()
    assert_solution(sol.containsDuplicate, arr, expected)
