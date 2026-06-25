class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        l, r = 0, len(people) - 1
        people.sort()
        while l <= r:

            if people[l] + people[r] > limit:
                r -= 1
            elif people[l] + people[r] <= limit:
                l, r = l + 1, r - 1
            boats += 1
            
        return boats
