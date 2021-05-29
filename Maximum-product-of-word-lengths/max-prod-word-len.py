import collections

def maxProd(words):
  lookup = collections.defaultdict(set)
  for w in words:
    lookup[w]=set(w)
  def common(s,t):
    if lookup[s]&lookup[t]:
      return False
    return True
  mx=0
  for i in words:
    for j in words:
      if common(i,j):
        mx=max(mx, len(i)*len(j))
  return mx
