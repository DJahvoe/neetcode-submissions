class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        data = self.data
        # ada key dalam data
        if not key in data:
            data[key] = {}    
            data[key]["prev_timestamp"] = []
        data[key]["prev_timestamp"].append(timestamp)
        data[key][timestamp] = value
        print(data)

    def get(self, key: str, timestamp: int) -> str:
        print("GET")
        data = self.data
        if key in data:
            # ada timestamp dalam data-key
            if timestamp in data[key]:
                return data[key][timestamp]
            # g ada timestamp dalam data-key
            else:
                # apabila timestamp lebih kecil dari prev_timestamp pertama, return null
                if timestamp <= data[key]["prev_timestamp"][0]:
                    return ""
                else:
                    prev_timestamp = data[key]["prev_timestamp"]
                    l = 0
                    r = len(prev_timestamp) - 1
                    while (r - l) > 1:
                        mid = (l + r) // 2
                        print("find timestamp")
                        print(l, r, mid)
                        if prev_timestamp[mid] < timestamp:
                            l = mid
                        else:
                            r = mid
                    print(l, r)
                    if prev_timestamp[r] <= timestamp:
                        return data[key][prev_timestamp[r]]
                    elif prev_timestamp[l] <= timestamp:
                        return data[key][prev_timestamp[l]]
                    else:
                        return ""
        else:
            return ""
            

        
