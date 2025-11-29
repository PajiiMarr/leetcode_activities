from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)



recentCounter = RecentCounter()

tests = [
    1,
    100,
    3001,
    3002,
    6000,
    7000,
    9000,
]

print("Testing RecentCounter:\n")

for t in tests:
    result = recentCounter.ping(t)
    print(f"ping({t}) -> {result}")
