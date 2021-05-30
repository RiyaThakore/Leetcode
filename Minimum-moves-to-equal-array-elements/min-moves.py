class Solution:
  def minMoves(nums):
    nums.sort()
    mid = int(len(nums)/2)
    moves = 0
    for i in range(len(nums)):
      moves = moves + abs(nums[mid] - nums[i])
    return(moves)
