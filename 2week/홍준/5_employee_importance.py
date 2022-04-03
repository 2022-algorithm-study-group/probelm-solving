"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        get_employee = {employee.id : employee for employee in employees}
        answer = 0
        q = deque([id])
        while q:
            node = get_employee[q.popleft()]
            answer += node.importance
            for sub in node.subordinates:
                q.append(sub)
        return answer