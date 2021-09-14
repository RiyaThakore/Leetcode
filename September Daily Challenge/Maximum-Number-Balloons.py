class Solution(object):
    def maxNumberOfBalloons(self, text):
        c=Counter(text)
        output=float('inf')
        for l in 'balon':
            if l in 'ban':
                output=min(output, c[l])
            else:
                output=min(output, c[l]//2)
        return output
        
