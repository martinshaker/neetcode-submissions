"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i:i.start)
        print(intervals)

        if not intervals:
            return True
        
        for i in range(0,len(intervals)-1):
            if intervals[i+1].start < intervals[i].end:
                return False
        return True
