class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # check if groupSize possible
        if len(hand) % groupSize != 0:
            return False
        
        # count for each elements
        hCounter = defaultdict(int)
        for h in hand:
            hCounter[h] += 1


        while len(hCounter) > 0:
            print(hCounter)
            print(hCounter.keys())
            minKey = min(hCounter.keys())
            for i in range(minKey, minKey + groupSize):
                if i not in hCounter:
                    return False
                hCounter[i] -= 1
                if hCounter[i] == 0:
                    del hCounter[i]

        return True
