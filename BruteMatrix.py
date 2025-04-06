class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, j, prev):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prev:
                return 0
            max_len = 0
            for dx, dy in directions:
                max_len = max(max_len, dfs(i+dx, j+dy, matrix[i][j]))
            return max_len + 1

        max_path = 0
        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j, -2147483648))
        return max_path
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # Output: 4
    print(solution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  # Output: 4
    print(solution.longestIncreasingPath([[1]]))  # Output: 1
    print(solution.longestIncreasingPath([[7,8,9],[5,6,7],[4,5,6]]))  # Output: 3
    print(solution.longestIncreasingPath([[1,2],[3,4]]))  # Output: 4