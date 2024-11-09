class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        altitude = 0
        for i in gain:
            altitude = altitude+i
            if altitude > m:
                m = altitude
        return m