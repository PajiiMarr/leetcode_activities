class NestedInteger:
    def __init__(self, value=None):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        elif isinstance(value, list):
            self._integer = None
            self._list = [v if isinstance(v, NestedInteger) else NestedInteger(v) 
                          for v in value]
        else:
            self._integer = None
            self._list = None

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        return self._integer

    def getList(self):
        return self._list


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]): # type: ignore
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True

            self.stack.pop()
            inner_list = top.getList()

            for item in reversed(inner_list):
                self.stack.append(item)

        return False
    
    
def build_nested_list(data):
    return NestedInteger(data).getList()

print("TEST 1: [[1,1],2,[1,1]]")
nestedList1 = build_nested_list([[1,1], 2, [1,1]])
i = NestedIterator(nestedList1)
result1 = []
while i.hasNext():
    result1.append(i.next())
print("Output:", result1)  


print("\nTEST 2: [1,[4,[6]]]")
nestedList2 = build_nested_list([1, [4, [6]]])
i = NestedIterator(nestedList2)
result2 = []
while i.hasNext():
    result2.append(i.next())
print("Output:", result2) 


print("\nTEST 3: []")
nestedList3 = build_nested_list([])
i = NestedIterator(nestedList3)
result3 = []
while i.hasNext():
    result3.append(i.next())
print("Output:", result3)


print("\nTEST 4: [[],[1,[2,3]],4]")
nestedList4 = build_nested_list([[], [1, [2, 3]], 4])
i = NestedIterator(nestedList4)
result4 = []
while i.hasNext():
    result4.append(i.next())
print("Output:", result4) 
