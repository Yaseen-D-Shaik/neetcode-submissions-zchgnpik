class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s_nums=[]
        for i in nums:
            i_s = str(i)
            s_nums.append(i_s)

        counts = {}

        for n in s_nums:
            counts[n] = counts.get(n, 0) + 1

        results= any(valus > 1 for valus in counts.values())

        return results
        
        

        
            
            
        