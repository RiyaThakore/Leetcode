class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        h=[]
        output, prev=0,0
        fuel=startFuel
        for dist, gas in stations+[[target,0]]:
          fuel-=(distance-prev)
          while h and fuel < 0:
            fuel+= -heappop(h)
            output +=1
          if fuel<0 :return -1
            heappush(h, -gas)
            prev=distance
        return(output)
