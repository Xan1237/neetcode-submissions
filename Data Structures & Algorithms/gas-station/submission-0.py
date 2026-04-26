class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalTrips = len(gas)
        currGas = 0
        currStation = 0
        numTrips = 0


        for i in range(0, totalTrips):
            currStation = i
            while currGas >= 0:
                currStation %= totalTrips
                currGas += (gas[currStation] - cost[currStation])
                if numTrips == totalTrips:
                    return i
                numTrips +=1
                currStation+=1
            numTrips = 0
            currGas = 0
        return -1
