class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
          "..",".---","-.-",".-..","--","-.","---",".--.",
          "--.-",".-.","...","-","..-","...-",".--","-..-",
          "-.--","--.."]
        
        letters = 'abcdefghijklmnopqrstuvwxyz'     
        l_to_m = {l: m for l, m in zip(letters, morse)}
        
        return len(set([''.join([l_to_m[ch] for ch in word]) for word in words]))
