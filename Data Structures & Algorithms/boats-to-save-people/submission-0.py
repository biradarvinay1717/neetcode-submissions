class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        cnt = 0
        people.sort()
        l, r = 0, len(people)-1

        while l <= r:
            if people[l] + people[r] <= limit:
                cnt += 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                r -= 1
                cnt += 1

        return cnt

        
