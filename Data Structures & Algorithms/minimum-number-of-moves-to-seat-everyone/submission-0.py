class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #maybe hashmap of seat keeping track of whether they have been sat in or not
        seats.sort()
        students.sort()
        res = 0
        for i in range(len(seats)):
            res += abs(seats[i] - students[i])
        return res