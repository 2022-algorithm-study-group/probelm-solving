"""
# Definition for Employee.
"""
from typing import List
from collections import deque


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        employee_dict = {}
        for employee in employees:
            employee_dict[employee.id] = employee
        ans = 0
        que = deque({id})
        while que:
            em = employee_dict[que.popleft()]
            ans += em.importance
            for s in em.subordinates:
                que.append(s)
        return ans
