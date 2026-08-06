'''class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        result = [0] * n
        
        # Base case: if k is 0, all values become 0
        if k == 0:
            return result
        
        # Define initial window range [left, right] for index 0
        if k > 0:
            left, right = 1, k
        else:
            left, right = n - abs(k), n - 1
            
        # Calculate sum of the initial window
        window_sum = sum(code[i % n] for i in range(left, right + 1))
        
        # Slide the window across all n elements
        for i in range(n):
            result[i] = window_sum
            
            # Slide window: remove code[left] and add code[right + 1]
            window_sum -= code[left % n]
            left += 1
            right += 1
            window_sum += code[right % n]
            
        return result
#1652

'''