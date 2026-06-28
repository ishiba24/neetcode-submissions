class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #take the max gas out of all possible positions? calculate gas by doing current - cost to next?
        if sum(gas) < sum(cost):
            return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                res = i + 1
        return res