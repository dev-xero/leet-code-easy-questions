def sumDigits(num: int) -> int:
  return sum([int(i) for i in str(num)]) if num != 0 else 0

class Solution:
    def addDigits(self, num: int) -> int:
        return sumDigits(num) if len(str(sumDigits(num))) == 1 else self.addDigits(sumDigits(num))
