from typing import List, Any
from ..utils.testing_helper import assert_solution
import pytest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Method1: compare sets
        # return set(s) == set(t)

        # Method2: use count dict
        f1 = {}
        for i in range(len(s)):
            f1[s[i]] = f1.get(s[i], 0) + 1
        f2 = {}
        for i in range(len(t)):
            f2[t[i]] = f2.get(t[i], 0) + 1
        return f1 == f2


test_cases: list[tuple[Any, Any]] = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
]


@pytest.mark.parametrize("arr, expected", test_cases)
def test_solution(arr, expected):
    sol = Solution()
    assert_solution(sol.isAnagram, arr, expected)
