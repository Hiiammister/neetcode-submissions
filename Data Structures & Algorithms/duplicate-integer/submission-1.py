class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set() #create a hashset
        for n in nums: #traverse through the hashset, searching for duplicates
            if n in hashset: #if found n is a duplicate return True
                return True
            hashset.add(n) #add the no. if not there
        return False #return false
         