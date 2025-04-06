class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""

        # Create a DP table
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True  # Every single character is a palindrome

        for end in range(1, n):
            for begin in range(end):
                if s[begin] == s[end]:
                    if end - begin == 1 or dp[begin + 1][end - 1]:
                        dp[begin][end] = True
                        if end - begin + 1 > max_len:
                            max_len = end - begin + 1
                            start = begin

        return s[start:start + max_len]
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(solution.longestPalindrome("cbbd"))   # Output: "bb"
    print(solution.longestPalindrome("a"))      # Output: "a"
    print(solution.longestPalindrome("ac"))     # Output: "a" or "c"
    print(solution.longestPalindrome("racecar"))  # Output: "racecar"