"""
https://leetcode.com/problems/reverse-vowels-of-a-string/

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"

Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".

"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        string = list(s)
        vowels = [i for i in enumerate(s) if i[1] in 'aeiouAEIOU']
        for ix, char in zip([i[0] for i in vowels],
                            reversed([i[1] for i in vowels])):
            string[ix] = char
        return ''.join(string)
