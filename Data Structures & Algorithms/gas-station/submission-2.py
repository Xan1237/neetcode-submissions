class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalTrips = len(gas)
        currGas = 0
        currStation = 0
        numTrips = 0
        flag = 0
        nextStation = 0

        while numTrips < totalTrips:
            currStation %= totalTrips
            if currStation == 0 and numTrips == 0 and flag == 1:
                return -1
            if currStation == 0 and numTrips == 0:
                flag = 1
            currGas += (gas[currStation]-cost[currStation])
            if currGas < 0:
                currGas = 0
                numTrips = 0
                nextStation += 1
                currStation = nextStation
            else:
                currStation +=1
                numTrips +=1
        return nextStation

            
