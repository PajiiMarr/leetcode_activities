from collections import deque

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        # Move only when stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


# --------------------------------------------------
#               TEST CASES FOR MyQueue
# --------------------------------------------------

print("TEST CASES FOR MYQUEUE\n")

# Test Case 1: Basic push + peek
print("Test Case 1: Push and Peek")
q = MyQueue()
q.push(1)
q.push(2)
print("Peek:", q.peek())   # Expected: 1
print()

# Test Case 2: Pop operation
print("Test Case 2: Pop")
print("Pop:", q.pop())     # Expected: 1
print("Peek:", q.peek())   # Expected: 2
print()

# Test Case 3: Empty check
print("Test Case 3: Empty Check")
print("Is empty?", q.empty())  # Expected: False
q.pop()
print("Is empty?", q.empty())  # Expected: True
print()

# Test Case 4: Push after emptying
print("Test Case 4: Push After Emptying")
q.push(5)
q.push(10)
print("Peek:", q.peek())   # Expected: 5
print("Pop:", q.pop())     # Expected: 5
print("Pop:", q.pop())     # Expected: 10
print("Is empty?", q.empty())  # Expected: True
print()

# Test Case 5: Sequential Operations
print("Test Case 5: Sequential Operations")
q.push(3)
q.push(6)
q.push(9)
print("Peek:", q.peek())   # Expected: 3
print("Pop:", q.pop())     # Expected: 3
print("Peek:", q.peek())   # Expected: 6
print("Pop:", q.pop())     # Expected: 6
print("Peek:", q.peek())   # Expected: 9
print("Is empty?", q.empty())  # Expected: False
