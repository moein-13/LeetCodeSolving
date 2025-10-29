class Solution:
    def maxProfit(self, prices: List[int]) -> int:

    ## Dynamic programming solution
    
        """komDam = prices[0]
        motLabh = 0 

        for sell in prices:

            Labh = sell - komDam
            motLabh = max(motLabh , Labh)
            komDam = min(komDam , sell)

        return motLabh
        """
        # Two pointer solution 
        bam , dan = 0 , 1

        motLabh = 0

        while dan < len(prices):
            if prices[bam] < prices[dan]:

                Labh = prices[dan] - prices[bam]
                motLabh = max(motLabh , Labh)
            else:
                bam = dan
            dan += 1

        return motLabh



            
       

