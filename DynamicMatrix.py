class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        memo = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]

            max_len = 1
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(x, y))

            memo[i][j] = max_len
            return max_len

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        return result
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # Output: 4
    print(solution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  # Output: 4
    print(solution.longestIncreasingPath([[1]]))  # Output: 1
    print(solution.longestIncreasingPath([[7,8,9],[5,6,7],[4,5,6]]))  # Output: 3
    print(solution.longestIncreasingPath([[1,2],[3,4]]))  # Output: 4
    print(solution.longestIncreasingPath([[1,2,3],[6,5,4],[7,8,9]]))  # Output: 9