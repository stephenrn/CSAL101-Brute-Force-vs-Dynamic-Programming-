class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ""  # Return an empty string if the input is empty

        # Create a DP table to store whether s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        start = 0  # Start index of the longest palindromic substring
        max_len = 1  # Length of the longest palindromic substring

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check all substrings of length 2 or more
        for end in range(1, n):
            for begin in range(end):
                # A substring is a palindrome if:
                # 1. The characters at the beginning and end are the same
                # 2. The substring between them is also a palindrome
                if s[begin] == s[end]:
                    if end - begin == 1 or dp[begin + 1][end - 1]:  # Two characters or inner substring is a palindrome
                        dp[begin][end] = True
                        # Update the longest palindrome if the current one is longer
                        if end - begin + 1 > max_len:
                            max_len = end - begin + 1
                            start = begin

        # Return the longest palindromic substring
        return s[start:start + max_len]
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(solution.longestPalindrome("cbbd"))   # Output: "bb"
    print(solution.longestPalindrome("a"))      # Output: "a"
    print(solution.longestPalindrome("ac"))     # Output: "a" or "c"
    print(solution.longestPalindrome("racecar"))  # Output: "racecar"