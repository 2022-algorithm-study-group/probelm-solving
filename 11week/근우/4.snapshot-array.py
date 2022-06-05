## https://leetcode.com/problems/snapshot-array/

from bisect import bisect, bisect_left
from collections import defaultdict


class SnapshotArray:
    class _SnapInfo:
        def __init__(self, snap_id: int, val: int):
            self.snap_id = snap_id
            self.val = val

    def __init__(self, length: int):
        self.arr = [[] for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append(self._SnapInfo(self.snap_id, val))

    def snap(self) -> int:
        self.snap_id +=1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self._bisect_left(index,snap_id)

    def _bisect_left(self, index, snap_id) -> int:
        snap_infos = self.arr[index]
        l, r = 0, len(snap_infos) - 1
        while l<r:
            m = (l+r)>>1
            if snap_infos[m].snap_id > snap_id:
                r = m
            else:
                l = m + 1
        return snap_infos[l].val





# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(length)
obj.set(index,val)
param_2 = obj.snap()
param_3 = obj.get(index,snap_id)

# from bisect import bisect
# from operator import attrgetter

# class SnapInfo:
#     def __init__(self, snap_id: int, val: int):
#         self.snap_id = snap_id
#         self.val = val

# a = [SnapInfo(1,2),SnapInfo(11,2),SnapInfo(3,1),SnapInfo(0,4)]
# print(a[bisect(a,2,key = attrgetter("snap_id"))])