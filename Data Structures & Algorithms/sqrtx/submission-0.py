class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # The square root of 0 is 0, and 1 is 1
            
        l, r = 1, x // 2  # The square root of x (where x >= 2) is always <= x // 2
        ans = 0
        
        while l <= r:
            mid = l + (r - l) // 2
            
            # Check if mid is a valid square root candidate
            if mid <= x // mid:
                ans = mid     # Store mid as a potential answer
                l = mid + 1   # Try to find a larger value in the right half
            else:
                r = mid - 1   # mid is too large, search the left half
                
        return ans