class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if len(words) == 1:
          return words
        
        else:
          return [words[i] for i in range(len(words)) if words[i] in ' '.join(words[:i]+words[i+1:])]
