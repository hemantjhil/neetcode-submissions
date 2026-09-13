class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the interval basis their starting val
        intervals.sort(key=lambda x:x[0])
        # create list for returning final list
        merged=[]
        for interval in intervals:
            # if merged empty or
            # if last add merge end val less than curr interval start val
            # mean no overlap add interval to merged
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            # make the last merged end val to max of curr interval
            # end val and last merged end val 
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        # return the final merge list 
        return merged
        