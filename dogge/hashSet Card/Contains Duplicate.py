#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> bool:
        s = set()
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                return True
        return False
