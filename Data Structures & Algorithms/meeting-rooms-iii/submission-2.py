class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        used = []

        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free every room that finished before this meeting starts
            while used and used[0][0] <= start:
                endTime, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if available:
                # Take smallest available room number
                room = heapq.heappop(available)

                heapq.heappush(used, (end, room))

            else:
                # No rooms available, delay meeting
                oldEnd, room = heapq.heappop(used)

                newEnd = oldEnd + duration

                heapq.heappush(used, (newEnd, room))

            count[room] += 1

        return count.index(max(count))
            
            