class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        total_cost = 0
        start_idx = 0
        tank = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

        # If the current tank becomes negative, update the start index and reset the tank
            if tank < 0:
                start_idx = i + 1
                tank = 0

    # If total_gas is less than total_cost, it's impossible to complete the circuit
        if total_gas < total_cost:
            return -1
        else:
            return start_idx

        