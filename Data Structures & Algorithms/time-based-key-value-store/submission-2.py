class TimeMap:

    def __init__(self):
        # key: list of [val, timestamp]
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # ada key dalam data
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([value, timestamp])
        print(self.data)

    def get(self, key: str, timestamp: int) -> str:
        print("GET")
        data = self.data

        result, values = "", data.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result
            
            

        
