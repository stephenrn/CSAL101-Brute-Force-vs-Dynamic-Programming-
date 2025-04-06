# Think-Pair-Share: Brute Force vs Dynamic Programming

### Stephen Raine Villeta | Jeferson Ruiz Cabalsa

## Objective:
In this activity, you will work with a partner to solve two algorithmic problems using both brute force and dynamic programming (DP) approaches. After solving and comparing the solutions, you will present your findings to the class, analyzing the efficiency of both approaches.

## Instructions:
- Pair up with another student.
- You will be given two problems to solve:
  1. **Longest Increasing Path in a Matrix**  
     [Problem Link]  
     Given an `m x n` integers matrix, return the length of the longest increasing path in the matrix.  
     From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wraparound is not allowed).  
     - **Example 1:**  
       Input: `matrix = [[9,9,4],[6,6,8],[2,1,1]]`  
       Output: `4`  
       Explanation: The longest increasing path is `[1, 2, 6, 9]`.  
     - **Example 2:**  
       Input: `matrix = [[3,4,5],[3,2,6],[2,2,1]]`  
       Output: `4`  
       Explanation: The longest increasing path is `[3, 4, 5, 6]`. Moving diagonally is not allowed.  
     - **Example 3:**  
       Input: `matrix = [[1]]`  
       Output: `1`  
     - **Constraints:**  
       - `m == matrix.length`  
       - `n == matrix[i].length`  
       - `1 <= m, n <= 200`  
       - `0 <= matrix[i][j] <= 2^31 − 1`  

  2. **Longest Palindromic Substring**  
     [Problem Link]  
     Given a string `s`, return the longest palindromic substring in `s`.  
     - **Example 1:**  
       Input: `s = "babad"`  
       Output: `"bab"`  
       Explanation: `"aba"` is also a valid answer.  
     - **Example 2:**  
       Input: `s = "cbbd"`  
       Output: `"bb"`  
     - **Constraints:**  
       - `1 <= s.length <= 1000`  
       - `s` consists of only digits and English letters.

- Assign roles:
  - One partner will work on the brute force solution for one problem, while the other works on the dynamic programming (DP) solution for the same problem.
  - Switch roles for the second problem: the partner who worked on the brute force solution will now work on the DP solution, and vice versa.
- Solve each problem using both approaches: brute force and dynamic programming.
  - For each problem:
    - **Brute Force**: Write a solution without optimization, focusing on the simplest way to solve the problem.
    - **Dynamic Programming**: Write an optimized solution using dynamic programming (memoization or tabulation).
- Discuss the approaches within your pair:
  - What is the brute force solution, and how does it work?
  - What is the dynamic programming solution, and how does it improve upon the brute force approach?
  - Compare the time and space complexities of both solutions. Is the DP solution faster or more efficient? Why?
- Present your solutions to the class:
  - Explain both the brute force and dynamic programming approaches clearly.
  - Discuss the time and space complexities of both solutions.
  - Share any observations on how dynamic programming optimizes the problem and reduces computational costs.

## Note:
- Keep your presentation concise but informative.
- Focus on the key differences between the brute force and dynamic programming solutions.
- Make sure your explanation of the complexities is clear to the class.

## Criteria

| Criteria                  | Description                                                                 | Points |
|---------------------------|-----------------------------------------------------------------------------|--------|
| **Solution Completeness** | Both brute force and dynamic programming solutions are correct and complete. | 20     |
| **Approach Explanation**  | Clear explanation of both the brute force and dynamic programming approaches. | 20     |
| **Time Complexity Analysis** | Accurate analysis of time complexity for both the brute force and dynamic programming approaches. | 20     |
| **Space Complexity Analysis** | Accurate analysis of space complexity for both the brute force and dynamic programming approaches. | 15     |
| **Comparison and Observations** | Detailed comparison of the brute force vs. dynamic programming approaches. | 15     |
| **Presentation and Clarity** | Clear, concise, and well-organized presentation.                          | 10     |
| **Total**                 |                                                                             | **100** |

## Additional Resources
For a general explanation of brute force and dynamic programming concepts, refer to the [Brute Force vs Dynamic Programming Overview](./BruteForce_vs_DP_Overview.md).
