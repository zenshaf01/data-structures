class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        firstBad = None

        if n == 1 and self.isBadVersion(n):
            return n

        while low <= high:
            mid = (low + high) // 2
            if self.isBadVersion(mid):
                firstBad = mid
                high = mid - 1
            elif not self.isBadVersion(mid):
                low = mid + 1
        return firstBad
    
    #Stub, Needs iomplementation
    def isBadVersion(n):
        return True