class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        n = len(arr)
        prevIndex = {}  
        dp = [0] * n
        ans = 0
        for i in range(n):
            prevNum = arr[i] - difference
            if prevNum in prevIndex: 
                dp[i] = dp[prevIndex[prevNum]] + 1
            else:
                dp[i] = 1
            prevIndex[arr[i]] = i 
            ans = max(ans, dp[i])
        return ans
