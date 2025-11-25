from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    if not arr:
        return None
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


if __name__ == "__main__":
    s = Solution()

    # Test Case 1
    lists1 = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]
    result1 = s.mergeKLists(lists1)
    print(linked_list_to_list(result1))

    lists2 = []
    result2 = s.mergeKLists(lists2)
    print(linked_list_to_list(result2))

    lists3 = [build_linked_list([])]
    result3 = s.mergeKLists(lists3)
    print(linked_list_to_list(result3))
