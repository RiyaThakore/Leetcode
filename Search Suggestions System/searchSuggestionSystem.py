class Solution(object):
    def suggestedProducts(self, products, searchWord):
        prod = sorted(products)
        output = [[] for _ in range(len(searchWord))]
        for i in range(len(searchWord)):
            for j in range(len(prod)):
                if searchWord[:i+1] in prod[j][:i+1] and len(output[i])<3:
                    output[i].append(prod[j])
        return(output)
        
