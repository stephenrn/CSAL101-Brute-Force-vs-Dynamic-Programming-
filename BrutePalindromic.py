class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        n = len(s)
        max_len = 0
        result = ""
        
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > max_len:
                    max_len = len(substring)
                    result = substring
        return result
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(solution.longestPalindrome("cbbd"))   # Output: "bb"
    print(solution.longestPalindrome("a"))      # Output: "a"
    print(solution.longestPalindrome("ac"))     # Output: "a" or "c"
    print(solution.longestPalindrome("racecar"))  # Output: "racecar"