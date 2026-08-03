"fruit into basket"
'''class Solution:
    def totalFruit(self, f: List[int]) -> int:
        left,ans = 0,0
        freq = {}
        for right in range(len(f)):
            freq[f[right]] = freq.get(f[right],0) + 1
            while len(freq) > 2:
                freq[f[left]] -= 1
                if freq[f[left]] == 0:
                    del freq[f[left]]
                left += 1
            ans = max(ans,right - left+1)
        return ans'''
        