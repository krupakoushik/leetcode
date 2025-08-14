class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        num
        best = ""

        for i in range(len(num) - 2):
            sub = num[i : i+3]
            if sub == sub[0] * 3:
                if sub > best:
                    best = sub
                    print best
            else:
                print("")

        return best
        

   
