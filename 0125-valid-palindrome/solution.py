class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s

        t = ''.join(c.lower()
                    for c in s
                        if c.isalnum())

        return t[:] == t[::-1]
        
