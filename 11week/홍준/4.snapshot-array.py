## https://leetcode.com/problems/snapshot-array/

from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.now = defaultdict(int)
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.now[index] = val

    def snap(self) -> int:
        snap = defaultdict(int)
        for key in self.now.keys():
            snap[key] = self.now[key]
        self.snaps.append(snap)
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)