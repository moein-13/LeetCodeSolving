class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    ## Dynamic programming solution
        komDam = prices[0]
        motLabh = 0 

        for sell in prices:

            Labh = sell - komDam
            motLabh = max(motLabh , Labh)
            komDam = min(komDam , sell)

        return motLabh

            
       

