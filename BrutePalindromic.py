class Solution(object):
    def longestPalindrome(self, s):
        """
        Finds the longest palindromic substring in the given string.
        :type s: str
        :rtype: str
        """
        def is_palindrome(sub):
            # Helper function to check if a substring is a palindrome.
            # A string is a palindrome if it reads the same forwards and backwards.
            return sub == sub[::-1]
        
        n = len(s)  # Length of the input string.
        max_len = 0  # Variable to store the length of the longest palindrome found.
        result = ""  # Variable to store the longest palindromic substring.
        
        # Iterate over all possible starting indices of substrings.
        for i in range(n):
            # Iterate over all possible ending indices of substrings starting from i.
            for j in range(i, n):
                substring = s[i:j+1]  # Extract the substring from index i to j (inclusive).
                # Check if the substring is a palindrome and if it is longer than the current max length.
                if is_palindrome(substring) and len(substring) > max_len:
                    max_len = len(substring)  # Update the maximum length.
                    result = substring  # Update the result with the new longest palindrome.
        return result  # Return the longest palindromic substring.
    
# Example usage:
if __name__ == "__main__":
    solution = Solution()
    # Test cases to demonstrate the functionality of the method.
    print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
    print(solution.longestPalindrome("cbbd"))   # Output: "bb"
    print(solution.longestPalindrome("a"))      # Output: "a"
    print(solution.longestPalindrome("ac"))     # Output: "a" or "c"
    print(solution.longestPalindrome("racecar"))  # Output: "racecar"