class SnapshotArray:
    def __init__(self, length: int):
        self.vals = [0] * length
        self.snaps = [[] for _ in range(length)]
        self.cur_snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.vals[index] = val

    def snap(self) -> int:
        for i, val_hist in enumerate(self.snaps):
            if len(val_hist) == 0 or val_hist[-1][0] != self.vals[i]:
                val_hist.append([self.vals[i], self.cur_snap_id])

        self.cur_snap_id += 1
        return self.cur_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        val_hist = self.snaps[index]

        lo, hi = 0, len(val_hist) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            mid_snap_id = val_hist[mid][1]

            if mid_snap_id > snap_id:
                hi = mid - 1
            else:
                lo = mid + 1

        return val_hist[hi][0]



def test():
    sa = SnapshotArray(3)
    sa.set(0, 5)
    sa.snap()
    sa.set(0, 6)
    assert sa.get(0, 0) == 5