class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key = lambda x: x[1])
        output,box=0,0
        for i in range(len(boxTypes)-1,-1,-1):
            box+=boxTypes[i][0]
            if box < truckSize:
                output+=(boxTypes[i][0]*boxTypes[i][1])
            else:
                output+=((truckSize-(box-boxTypes[i][0]))*boxTypes[i][1])
                return (output)
                break
        return (output)
        
