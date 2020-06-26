"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false

"""


import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(re.findall(r'[a-z0-9]', s.lower()))
        return s == s[::-1]
