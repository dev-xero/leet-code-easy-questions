class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) < 2: return A
        
        a_list = set(A[0])
        res = []
        
        for ch in a_list:
            n = min([a_word.count(ch) for a_word in A])
            if n:
                res += [ch]*n
                
        return res
