Given a rectangular cake with height h and width w, and two arrays of integers `horizontalCuts` and `verticalCuts` where `horizontalCuts[i]` is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, `verticalCuts[j]` is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays `horizontalCuts` and `verticalCuts`. Since the answer can be a huge number, return this modulo 10^9 + 7.

#### Example 1:

Input: <br>
h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3] <br>

Output: <br>
4 <br>

Explanation: <br>
The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.

(Updated) Result:
It is important to pay attention to the details of answers especially regarding 'modulo 10^9 + 7'  <br>
Time Complexity: O(n log n) + O(m log m) 
