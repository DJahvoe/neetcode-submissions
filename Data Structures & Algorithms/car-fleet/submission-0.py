class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position) - 1):
            for j in range(len(position) - 1):
                if position[j] < position[j+1]:
                    temp = position[j]
                    position[j] = position[j+1]
                    position[j+1] = temp

                    temp = speed[j]
                    speed[j] = speed[j+1]
                    speed[j+1] = temp
        timeArrived = []
        for t in range(len(position)):
            timeArrived.append((target - position[t]) / speed[t])

        fleetCount = 0
        maxTime = 0
        for t in timeArrived:
            if t > maxTime:
                fleetCount += 1
                maxTime = t
        print(position)
        print(speed)
        print(timeArrived)
        return fleetCount
