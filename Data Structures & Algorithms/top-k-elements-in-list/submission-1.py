class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} #create hashmap/ dict
        freq=[[]for i in range(len(nums)+1)] #create a list of empty list
        for n in nums: #traverse through the list
            count[n]=1+count.get(n,0) #update the frequency
        for n,c in count.items(): #traverse inside the dict
            freq[c].append(n)#place the values and their corresponding freq in the dict/bucket
        res=[]#create for result
        for i in range(len(freq)-1, 0, -1):#check in a desc value
            for n in freq[i]: #check all nums with k elements
                res.append(n)
                if len(res)==k:#stop when k is complete
                    return res
        