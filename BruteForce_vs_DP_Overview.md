# Brute Force vs Dynamic Programming: Core Concepts

## 💥 Brute Force Solution

### Explanation:
The brute force approach explores all possible solutions without optimization:
- For **Longest Increasing Path in a Matrix**, it uses a depth-first search (DFS) to explore all paths starting from each cell. It does not store intermediate results, leading to repeated computations for overlapping subproblems.
- For **Longest Palindromic Substring**, it checks every possible substring to determine if it is a palindrome, using a helper function to verify each substring.

### Time and Space Complexities:
- **Longest Increasing Path in a Matrix**:
  - **Time Complexity**: `O(4^(m*n))` in the worst case, as each cell can branch into 4 directions recursively.
  - **Space Complexity**: `O(m*n)` for the recursion stack in the worst case.
- **Longest Palindromic Substring**:
  - **Time Complexity**: `O(n^3)` because it checks all substrings (`O(n^2)`) and verifies each substring (`O(n)`).
  - **Space Complexity**: `O(1)` as no additional data structures are used.

---

## ⚡ Dynamic Programming (DP) Solution

### Explanation:
The dynamic programming approach optimizes by storing solutions to subproblems:
- For **Longest Increasing Path in a Matrix**, it uses memoization to store the length of the longest path starting from each cell. This avoids redundant computations for overlapping subproblems.
- For **Longest Palindromic Substring**, it uses a 2D table (`dp`) where `dp[i][j]` indicates whether the substring `s[i:j+1]` is a palindrome. It builds the solution iteratively, ensuring each subproblem is solved only once.

### Time and Space Complexities:
- **Longest Increasing Path in a Matrix**:
  - **Time Complexity**: `O(m*n)` because each cell is visited once, and its result is stored.
  - **Space Complexity**: `O(m*n)` for the memoization table.
- **Longest Palindromic Substring**:
  - **Time Complexity**: `O(n^2)` because it fills a 2D table for all substrings.
  - **Space Complexity**: `O(n^2)` for the DP table.

---

## 🔍 Observations

1. **Optimization**:
   - Dynamic programming avoids redundant computations by storing intermediate results, significantly reducing the time complexity compared to brute force.
   - For example, in the matrix problem, DP ensures each cell's result is computed only once, while brute force recomputes it multiple times.

2. **Trade-offs**:
   - DP solutions often require additional memory (e.g., memoization table or DP table), increasing space complexity compared to brute force.

3. **Efficiency**:
   - For large inputs, DP solutions are much faster due to their polynomial time complexity, while brute force solutions become infeasible due to exponential growth.

4. **Applicability**:
   - DP is ideal for problems with overlapping subproblems and optimal substructure, as seen in both the matrix and palindrome problems.

By leveraging dynamic programming, we achieve significant computational savings at the cost of additional memory usage.
