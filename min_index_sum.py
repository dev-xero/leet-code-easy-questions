class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
      common = set(list1) & set(list2)
      if len(common) > 1:
        res = []
        minimum = min([list1.index(i) + list2.index(i) for i in common])
        
        for item in common:
          curr_sum = sum([list1.index(item), list2.index(item)])

          if curr_sum == minimum:
            res.append(item)
            
        return res
      
      else:
        return common
