class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        i, j = 0, len(s)
        for c in s:
            if c == 'I':
                res.append(i)
                i += 1
            if c == 'D':
                res.append(j)
                j -= 1
                
        res.append(i)
        return res  
