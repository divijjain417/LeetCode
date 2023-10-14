class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sortedByFinishing = sorted(intervals, key = lambda x: x[1])
        finishingList = [interval[1] for interval in sortedByFinishing]

        optimal = [[0, sortedByFinishing[0]]]
        length = len(intervals)
        
        for index in range(1, length):
            interval = sortedByFinishing[index]

            previousOptimalSol = optimal[index - 1]
            previousOptimalLastInterval = previousOptimalSol[1]

            if previousOptimalLastInterval[1] <= interval[0]:
                optimal.append([previousOptimalSol[0], interval])
            else:
                fmaxIndex = bisect.bisect_right(finishingList, interval[0]) - 1
                intervalsRemoved = optimal[fmaxIndex][0]
                
                if fmaxIndex == -1:
                    if index <= previousOptimalSol[0] + 1:
                        optimal.append([index, interval])
                    else:
                        optimal.append([previousOptimalSol[0] + 1, previousOptimalSol[1]])

                elif (intervalsRemoved + index - fmaxIndex - 1 <= previousOptimalSol[0] + 1):
                    fmaxOptimal = optimal[fmaxIndex]
                    optimal.append([fmaxOptimal[0] + index - fmaxIndex - 1, interval])
                else:
                    optimal.append([previousOptimalSol[0] + 1, previousOptimalSol[1]])
         
        return optimal[-1][0]
        