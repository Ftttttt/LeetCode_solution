class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:  //零是回文数
            return True 
        if x < 0 or (x//10)*10 == x: //负数和末尾为零的数字不可能是回文数
            return False
        rev = 0
        while rev < x:
            rev = rev*10 + x % 10
            x //= 10
        return (rev == x) or (rev//10 == x) //如果x是偶数，rev==x可得True，x是奇数，则rev//10==x可得True

if __name__ == "__main__":
    print(Solution().isPalindrome(12321))
    print(Solution().isPalindrome(12320))
    print(Solution().isPalindrome(-12321))
