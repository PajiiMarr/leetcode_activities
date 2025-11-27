class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26

        # Count frequency
        for c in s:
            freq[ord(c) - ord('a')] += 1

        # Find first unique
        for i, c in enumerate(s):
            if freq[ord(c) - ord('a')] == 1:
                return i

        return -1


# ---------------------------
# Test Cases
# ---------------------------

solution = Solution()

tests = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
    ("z", 0),
    ("aaabcccdeeef", 3),   # 'b' is unique
    ("", -1),              # edge case: empty string
    ("abcabc", -1),        # no unique
    ("abc", 0),            # 'a' is unique
]

for s, expected in tests:
    result = solution.firstUniqChar(s)
    print(f"Input: {s:15} | Output: {result} | Expected: {expected}")
