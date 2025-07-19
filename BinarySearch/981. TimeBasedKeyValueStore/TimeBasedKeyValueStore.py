class TimeMap:
    def __init__(self):
        self.cache = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.cache.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if self.cache[m][1] <= timestamp:
                res = self.cache[m][0]
                l = m + 1
            else:
                r = r - 1
        return res

