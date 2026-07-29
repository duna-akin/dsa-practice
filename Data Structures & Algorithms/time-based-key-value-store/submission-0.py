class TimeMap:
    def __init__(self):
        self.keys = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        mostRecent = ""
        values = self.keys[key]
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                mostRecent = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return mostRecent

