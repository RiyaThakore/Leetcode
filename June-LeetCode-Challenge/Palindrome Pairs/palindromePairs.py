class Solution(object):
    def palindromePairs(self, words):
        d=dict([(w[::-1],i) for i,w in enumerate(words)])
        res=[]
        for i,w in enumerate(words):
            for j in range(len(w)+1):
                pre, post = w[:j], w[j:]
                if pre in d and i!=d[pre] and post == post[::-1]:
                    res.append([i, d[pre]])
                if j>0 and post in d and i!=d[post] and pre == pre[::-1]:
                    res.append([d[post],i])
        return(res)
        
