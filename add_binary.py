class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = []
        for i in reversed(range(n)):
            carry += int(a[i]) + int(b[i])
            answer.append(str(carry % 2))
            carry //= 2
            
        if carry:
            answer.append('1')
            
        return ''.join(answer[::-1])
