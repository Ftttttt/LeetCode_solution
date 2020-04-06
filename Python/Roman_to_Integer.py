class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst1 = ['I','V','X','L','C','D','M']
        lst3 = ['IV','IX','XL','XC','CD','CM']
        lst4 = [4, 9, 40, 90, 400, 900]
        res = 0
        if s in lst3:
            return lst4[lst3.index(s)]
        for i in range(len(lst3)):
            if lst3[i] in s:
                res += lst4[i]
                s = s[:s.index(lst3[i])] + s[s.index(lst3[i])+2:]
        dic_s = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for char in s:
            res += dic_s[char]
        return res


if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))
    print(Solution().romanToInt('IV'))
