class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0  # Return 0 if the matrix is empty

        m = len(matrix)  # Number of rows
        n = len(matrix[0])  # Number of columns
        # Directions for moving up, down, left, and right
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        # Memoization table to store the longest path starting from each cell
        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            # If the result for this cell is already computed, return it
            if memo[i][j] != 0:
                return memo[i][j]

            max_len = 1  # Minimum path length is 1 (the cell itself)
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                # Check if the next cell is within bounds and has a greater value
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    # Recursively compute the longest path from the next cell
                    max_len = max(max_len, 1 + dfs(x, y))

            # Store the result in the memoization table
            memo[i][j] = max_len
            return max_len

        result = 0  # Variable to store the overall longest path
        # Iterate through all cells in the matrix
        for i in range(m):
            for j in range(n):
                # Update the result with the longest path starting from the current cell
                result = max(result, dfs(i, j))
        return result  # Return the overall longest increasing path
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # Output: 4
    print(solution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  # Output: 4
    print(solution.longestIncreasingPath([[1]]))  # Output: 1
    print(solution.longestIncreasingPath([[7,8,9],[5,6,7],[4,5,6]]))  # Output: 3
    print(solution.longestIncreasingPath([[1,2],[3,4]]))  # Output: 4
    print(solution.longestIncreasingPath([[1,2,3],[6,5,4],[7,8,9]]))  # Output: 9