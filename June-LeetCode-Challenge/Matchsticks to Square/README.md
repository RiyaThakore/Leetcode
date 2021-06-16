You are given an integer array matchsticks where `matchsticks[i]` is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return `true` if you can make this square and `false` otherwise.

Input:
matchsticks = [1,1,2,2,2] <br>

Output:
True

Explanation: 
You can form a square with length 2, one side of the square came two sticks with length 1.

Update:<br>
Approach: Depth First Search
It is intuitive because we need to find the best combination for every matchstick amongst the four sides. To improve the recursion (memoization), we can sort the array in reverse order.

Time Complexity : O(4^N) <br>
Space Complexity : O(N)
