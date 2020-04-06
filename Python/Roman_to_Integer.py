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
        dic_s = {'I':0,'V':0,'X':0,'L':0,'C':0,'D':0,'M':0}
        for char in s:
            dic_s[char] += 1
        res += dic_s['I']*1 + dic_s['V']*5 + dic_s['X']*10 + dic_s['L']*50 + dic_s['C']*100 + dic_s['D']*500 + dic_s['M']*1000
        return res


if __name__ == '__main__':
    print(Solution().romanToInt('MCMXCIV'))
    print(Solution().romanToInt('IV'))
