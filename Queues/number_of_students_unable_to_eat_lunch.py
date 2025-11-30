from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        queue = deque(students)
        index = 0
        rotations = 0

        while queue and rotations < len(queue):
            if queue[0] == sandwiches[index]:
                queue.popleft()
                index += 1
                rotations = 0
            else:
                queue.append(queue.popleft())
                rotations += 1

        return len(queue)

solution = Solution()

tests = [
    ([1,1,0,0], [0,1,0,1], 0),
    ([1,1,1,0,0,1], [1,0,0,0,1,1], 3),
    ([0,1], [1,0], 2),
    ([1,0], [1,0], 0),
    ([0,0,0], [0,0,0], 0),
    ([1,1,1], [0,0,0], 3),
]

print("Running Test Cases:\n")
for students, sandwiches, expected in tests:
    result = solution.countStudents(students, sandwiches)
    print(f"students={students}, sandwiches={sandwiches} -> {result} (expected {expected})")
