class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] =[]
        self.map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        valkey = self.map.get(key,[])
        if not valkey or valkey[0][0] > timestamp: return ""
        l,r = 0, len(valkey) -1
        while l <= r:
            m = (l+r) // 2
            if valkey[m][0] == timestamp:
                return valkey[m][1]
            elif valkey[m][0] > timestamp:
                r = m-1
            else:
                l = m+1
        
        return valkey[r][1]
