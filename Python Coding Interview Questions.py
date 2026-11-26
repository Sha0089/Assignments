from collections import Counter, defaultdict, deque
import heapq


# 1. Find the second-largest unique element in an array without using sort() or max().
print("1. Find the second-largest unique element in an array without using sort() or max().")

def second_largest_unique(arr):
    first = second = float("-inf")
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return None if second == float("-inf") else second

print("Result:", second_largest_unique([10, 20, 4, 45, 99, 99, 45]))


# 2. Find all pairs in an array whose sum equals a given target.
print("\n2. Find all pairs in an array whose sum equals a given target.")

def find_pairs_with_sum(arr, target):
    seen = set()
    pairs = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return sorted(pairs)

print("Result:", find_pairs_with_sum([2, 4, 3, 5, 7, 8, -1], 7))


# 3. Move all zeros to the end of an array without changing the order of other elements.
print("\n3. Move all zeros to the end of an array without changing the order of other elements.")

def move_zeros_to_end(arr):
    arr = arr[:]
    insert_pos = 0
    for num in arr:
        if num != 0:
            arr[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(arr):
        arr[insert_pos] = 0
        insert_pos += 1
    return arr

print("Result:", move_zeros_to_end([0, 1, 0, 3, 12, 0, 5]))


# 4. Find the missing number from an array containing numbers from 1 to N.
print("\n4. Find the missing number from an array containing numbers from 1 to N.")

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)

print("Result:", find_missing_number([1, 2, 4, 5, 6], 6))


# 5. Find all duplicate elements in a list without using nested loops.
print("\n5. Find all duplicate elements in a list without using nested loops.")

def find_duplicates(arr):
    seen = set()
    duplicates = []
    added = set()
    for item in arr:
        if item in seen and item not in added:
            duplicates.append(item)
            added.add(item)
        seen.add(item)
    return duplicates

print("Result:", find_duplicates([1, 2, 3, 2, 4, 5, 1, 6, 2]))


# 6. Find the first non-repeating character in a string.
print("\n6. Find the first non-repeating character in a string.")

def first_non_repeating_char(s):
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None

print("Result:", first_non_repeating_char("swiss"))


# 7. Check whether two strings are anagrams without using sorted().
print("\n7. Check whether two strings are anagrams without using sorted().")

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1
    return True

print("Result:", are_anagrams("listen", "silent"))


# 8. Merge two sorted arrays without using sort().
print("\n8. Merge two sorted arrays without using sort().")

def merge_sorted_arrays(a, b):
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

print("Result:", merge_sorted_arrays([1, 3, 5, 7], [2, 4, 6, 8]))


# 9. Rotate an array to the right by K positions.
print("\n9. Rotate an array to the right by K positions.")

def rotate_right(arr, k):
    if not arr:
        return arr
    k %= len(arr)
    return arr[-k:] + arr[:-k] if k else arr[:]

print("Result:", rotate_right([1, 2, 3, 4, 5, 6, 7], 3))


# 10. Find the intersection of two arrays, including duplicate occurrences.
print("\n10. Find the intersection of two arrays, including duplicate occurrences.")

def array_intersection(a, b):
    counts = Counter(a)
    result = []
    for num in b:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return result

print("Result:", array_intersection([1, 2, 2, 1], [2, 2, 3]))


# 11. Find the maximum sum of a contiguous subarray.
print("\n11. Find the maximum sum of a contiguous subarray.")

def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print("Result:", max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# 12. Find the longest substring without repeating characters.
print("\n12. Find the longest substring without repeating characters.")

def longest_unique_substring(s):
    char_index = {}
    left = 0
    best_start = best_len = 0
    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        if right - left + 1 > best_len:
            best_len = right - left + 1
            best_start = left
    return s[best_start:best_start + best_len], best_len

print("Result:", longest_unique_substring("abcabcbb"))


# 13. Find the longest common prefix among multiple strings.
print("\n13. Find the longest common prefix among multiple strings.")

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

print("Result:", longest_common_prefix(["flower", "flow", "flight"]))


# 14. Group a list of strings into anagram groups.
print("\n14. Group a list of strings into anagram groups.")

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())

print("Result:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# 15. Find the Kth largest element in an unsorted array.
print("\n15. Find the Kth largest element in an unsorted array.")

def kth_largest(arr, k):
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

print("Result:", kth_largest([3, 2, 1, 5, 6, 4], 2))


# 16. Check whether a given string contains balanced parentheses using a stack.
print("\n16. Check whether a given string contains balanced parentheses using a stack.")

def is_balanced_parentheses(s):
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in matching:
            if not stack or stack.pop() != matching[ch]:
                return False
    return len(stack) == 0

print("Result:", is_balanced_parentheses("{[()]}"))


# 17. Find all subarrays whose sum equals a given target.
print("\n17. Find all subarrays whose sum equals a given target.")

def find_subarrays_with_sum(arr, target):
    prefix_map = defaultdict(list)
    prefix_map[0].append(-1)
    curr_sum = 0
    result = []
    for i, num in enumerate(arr):
        curr_sum += num
        if (curr_sum - target) in prefix_map:
            for start_idx in prefix_map[curr_sum - target]:
                result.append(arr[start_idx + 1:i + 1])
        prefix_map[curr_sum].append(i)
    return result

print("Result:", find_subarrays_with_sum([3, 4, -7, 1, 3, 3, 1, -4], 7))


# 18. Merge overlapping intervals in a list.
print("\n18. Merge overlapping intervals in a list.")

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged

print("Result:", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))


# 19. Search for an element in a rotated sorted array.
print("\n19. Search for an element in a rotated sorted array.")

def search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print("Result:", search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))


# 20. Find the longest consecutive sequence in an unsorted array.
print("\n20. Find the longest consecutive sequence in an unsorted array.")

def longest_consecutive_sequence(arr):
    num_set = set(arr)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr = num
            length = 1
            while curr + 1 in num_set:
                curr += 1
                length += 1
            longest = max(longest, length)
    return longest

print("Result:", longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))


# 21. Find the trapped rainwater between elevation bars.
print("\n21. Find the trapped rainwater between elevation bars.")

def trap_rainwater(heights):
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
            right -= 1
    return water

print("Result:", trap_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# 22. Find the median of two sorted arrays in O(log(m+n)) time.
print("\n22. Find the median of two sorted arrays in O(log(m+n)) time.")

def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    while low <= high:
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i
        max_left1 = float("-inf") if i == 0 else nums1[i - 1]
        min_right1 = float("inf") if i == m else nums1[i]
        max_left2 = float("-inf") if j == 0 else nums2[j - 1]
        min_right2 = float("inf") if j == n else nums2[j]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            return float(max(max_left1, max_left2))
        elif max_left1 > min_right2:
            high = i - 1
        else:
            low = i + 1
    return 0.0

print("Result:", find_median_sorted_arrays([1, 3], [2, 4]))


# 23. Find the maximum product of a contiguous subarray.
print("\n23. Find the maximum product of a contiguous subarray.")

def max_product_subarray(nums):
    cur_max = cur_min = ans = nums[0]
    for num in nums[1:]:
        candidates = (num, cur_max * num, cur_min * num)
        cur_max = max(candidates)
        cur_min = min(candidates)
        ans = max(ans, cur_max)
    return ans

print("Result:", max_product_subarray([2, 3, -2, 4]))


# 24. Find the smallest missing positive integer from an unsorted array.
print("\n24. Find the smallest missing positive integer from an unsorted array.")

def first_missing_positive(nums):
    nums = nums[:]
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target_idx = nums[i] - 1
            nums[i], nums[target_idx] = nums[target_idx], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

print("Result:", first_missing_positive([3, 4, -1, 1]))


# 25. Count the number of subarrays whose sum equals K.
print("\n25. Count the number of subarrays whose sum equals K.")

def count_subarrays_sum_k(nums, k):
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    curr_sum = count = 0
    for num in nums:
        curr_sum += num
        count += prefix_counts[curr_sum - k]
        prefix_counts[curr_sum] += 1
    return count

print("Result:", count_subarrays_sum_k([1, 1, 1], 2))


# 26. Find the longest increasing subsequence in an array.
print("\n26. Find the longest increasing subsequence in an array.")

def longest_increasing_subsequence(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print("Result:", longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))


# 27. Solve the Coin Change problem using dynamic programming.
print("\n27. Solve the Coin Change problem using dynamic programming.")

def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1

print("Result:", coin_change([1, 2, 5], 11))


# 28. Solve the Word Break problem using dynamic programming.
print("\n28. Solve the Word Break problem using dynamic programming.")

def word_break(s, word_dict):
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

print("Result:", word_break("leetcode", ["leet", "code"]))


# 29. Find the minimum number of jumps required to reach the last index.
print("\n29. Find the minimum number of jumps required to reach the last index.")

def min_jumps(nums):
    if len(nums) <= 1:
        return 0
    jumps = current_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps

print("Result:", min_jumps([2, 3, 1, 1, 4]))


# 30. Find the maximum profit from buying and selling stocks with multiple transactions.
print("\n30. Find the maximum profit from buying and selling stocks with multiple transactions.")

def max_stock_profit_multiple(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

print("Result:", max_stock_profit_multiple([7, 1, 5, 3, 6, 4]))


# 31. Implement an LRU Cache with O(1) time complexity for get() and put().
print("\n31. Implement an LRU Cache with O(1) time complexity for get() and put().")

class DListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = DListNode(key, value)
        self.cache[key] = node
        self._add_to_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

lru = LRUCache(2)
lru.put(1, 10)
lru.put(2, 20)
print("get(1):", lru.get(1))
lru.put(3, 30)
print("get(2) after eviction:", lru.get(2))


# 32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).
print("\n32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).")

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print("getMin():", ms.getMin())
ms.pop()
print("top():", ms.top(), "getMin():", ms.getMin())


# 33. Find the number of islands in a 2D matrix using DFS or BFS.
print("\n33. Find the number of islands in a 2D matrix using DFS or BFS.")

def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        while queue:
            cr, cc = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    return islands

sample_grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print("Result:", num_islands(sample_grid))


# 34. Find the shortest path in a weighted graph using Dijkstra's algorithm.
print("\n34. Find the shortest path in a weighted graph using Dijkstra's algorithm.")

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > distances[u]:
            continue
        for v, weight in graph[u]:
            new_dist = curr_dist + weight
            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return distances

weighted_graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [("F", 11)],
    "E": [("D", 4)],
    "F": [],
}
print("Result:", dijkstra(weighted_graph, "A"))


# 35. Detect a cycle in a directed and undirected graph.
print("\n35. Detect a cycle in a directed and undirected graph.")

def has_cycle_directed(graph):
    state = {}  # 0=unvisited, 1=visiting, 2=visited

    def dfs(u):
        state[u] = 1
        for v in graph.get(u, []):
            if state.get(v, 0) == 1:
                return True
            if state.get(v, 0) == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    for node in graph:
        if state.get(node, 0) == 0:
            if dfs(node):
                return True
    return False

def has_cycle_undirected(graph):
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

dir_graph = {0: [1], 1: [2], 2: [0]}
undir_graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
print("Directed cycle:", has_cycle_directed(dir_graph), "| Undirected cycle:", has_cycle_undirected(undir_graph))


# 36. Implement topological sorting for a directed acyclic graph.
print("\n36. Implement topological sorting for a directed acyclic graph.")

def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] = in_degree.get(v, 0) + 1
    queue = deque([u for u, deg in in_degree.items() if deg == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return order if len(order) == len(in_degree) else []

dag = {5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}
print("Result:", topological_sort(dag))


# 37. Solve the N-Queens problem using backtracking.
print("\n37. Solve the N-Queens problem using backtracking.")

def solve_n_queens(n):
    solutions = []
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            solutions.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)
            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return solutions

print("Result (N=4):", solve_n_queens(4))


# 38. Generate all permutations of a given string or array without duplicates.
print("\n38. Generate all permutations of a given string or array without duplicates.")

def unique_permutations(seq):
    items = sorted(seq)
    used = [False] * len(items)
    result = []
    path = []

    def backtrack():
        if len(path) == len(items):
            result.append("".join(path) if isinstance(seq, str) else path[:])
            return
        for i in range(len(items)):
            if used[i]:
                continue
            if i > 0 and items[i] == items[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(items[i])
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result

print("Result:", unique_permutations("aab"))


# 39. Serialize and deserialize a binary tree.
print("\n39. Serialize and deserialize a binary tree.")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize_tree(root):
    vals = []

    def preorder(node):
        if not node:
            vals.append("#")
            return
        vals.append(str(node.val))
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return ",".join(vals)

def deserialize_tree(data):
    tokens = iter(data.split(","))

    def build():
        val = next(tokens)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()

root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized = serialize_tree(root)
deserialized = deserialize_tree(serialized)
print("Serialized:", serialized, "| Re-serialized:", serialize_tree(deserialized))


# 40. Find the lowest common ancestor of two nodes in a binary tree.
print("\n40. Find the lowest common ancestor of two nodes in a binary tree.")

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right

node4 = TreeNode(4)
node5 = TreeNode(5)
node3 = TreeNode(3, node4, node5)
tree_root = TreeNode(1, TreeNode(2), node3)
lca = lowest_common_ancestor(tree_root, node4, node5)
print("LCA value:", lca.val if lca else None)
