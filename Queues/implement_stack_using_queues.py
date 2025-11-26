from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# ---------------------------------------
#               TEST CASES
# ---------------------------------------

print("TEST CASES FOR MYSTACK\n")

# Test Case 1: Basic Push and Top
print("Test Case 1: Push and Top")
s = MyStack()
s.push(1)
s.push(2)
print("Top:", s.top())     # Expected: 2
print()

# Test Case 2: Pop Operation
print("Test Case 2: Pop")
print("Pop:", s.pop())     # Expected: 2
print("Top:", s.top())     # Expected: 1
print()

# Test Case 3: Check Empty
print("Test Case 3: Empty Check")
print("Is empty?", s.empty())  # Expected: False
s.pop()
print("Is empty?", s.empty())  # Expected: True
print()

# Test Case 4: Push After Empty
print("Test Case 4: Push After Emptying")
s.push(5)
s.push(10)
print("Top:", s.top())     # Expected: 10
print("Pop:", s.pop())     # Expected: 10
print("Pop:", s.pop())     # Expected: 5
print("Is empty?", s.empty())  # Expected: True
print()

# Test Case 5: Multiple Sequential Operations
print("Test Case 5: Sequential Operations")
s.push(3)
s.push(7)
s.push(9)
print("Top:", s.top())     # Expected: 9
print("Pop:", s.pop())     # Expected: 9
print("Top:", s.top())     # Expected: 7
print("Pop:", s.pop())     # Expected: 7
print("Top:", s.top())     # Expected: 3
print("Is empty?", s.empty())  # Expected: False
print()
