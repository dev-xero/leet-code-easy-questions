class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:        
        m, n = len(strs), len(strs[0])
        res = 0
        
        for i in range(n):
            for j in range(m-1):
                if strs[j][i]> strs[j+1][i]:
                    res += 1
                    break
                    
        return res
