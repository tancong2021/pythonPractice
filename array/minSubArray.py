from typing import List

class Solution:
    def minSubArray(self, nums: List[int], target: int) -> int:
        left = 0
        total = 0
        min_len = float('inf')
        for right in range(len(nums)):
            total += nums[right]                      # 右边界元素进窗口
            while total >= target:                    # 满足条件就尽量收缩左边界
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArray([2, 3, 1, 2, 4, 3], 7))   # 2（子数组 [4,3]）