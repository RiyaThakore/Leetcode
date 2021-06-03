class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        horizontalCuts=[0]+horizontalCuts+[h]
        horizontalCuts.sort()
        verticalCuts=[0]+verticalCuts+[w]
        verticalCuts.sort()
        wt,ht=0,0
        for i in range(1,len(horizontalCuts)):
            wt=max(wt, abs(horizontalCuts[i-1]-horizontalCuts[i]))
        for i in range(1,len(verticalCuts)):
            ht=max(ht, abs(verticalCuts[i-1]-verticalCuts[i]))
        return(wt*ht)%(10**9+7)
        
