Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u') <br>
Each vowel 'a' may only be followed by an 'e'.<br>
Each vowel 'e' may only be followed by an 'a' or an 'i'.<br>
Each vowel 'i' may not be followed by another 'i'.<br>
Each vowel 'o' may only be followed by an 'i' or a 'u'.<br>
Each vowel 'u' may only be followed by an 'a'.<br>
Since the answer may be too large, return it modulo 10^9 + 7.<br>

Example 1:

Input: n = 2 <br>
Output: 10 <br>
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua". <br>

`Solution:`
This probem has transtions of trees/directed graphs. Keep track of number of each vowel in every level of this tree.

