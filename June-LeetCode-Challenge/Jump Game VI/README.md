You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range `[i + 1, min(n - 1, i + k)]` inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

*Return the maximum score you can get.*

### Input:
nums = [1,-1,-2,4,-7,3], k = 2

### Output:
7

### Explanation:
You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.

<br>
This is solved by Dynamic Programming problem with Dequeue. Naive DP approach increases space complexity.<br>
Similar problem: "Maximum in Sliding Window Size k" problem
<br><br>

Complexity:

Time: O(N * K), where N <= 10^5 is number of elements in nums, K <= 10^5 is the maximum steps that we can jump. <bbr>
Space: O(N)
