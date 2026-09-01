class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key]:
            return ""
        
        l = 0
        r = len(self.d[key])

        arr = self.d[key]

        while l < r:
            m = (l + r) // 2

            time = arr[m][1]
            if time <= timestamp:
                l = m + 1
            else:
                r = m 
        
        return arr[l - 1][0] if l > 0 else ""

        
