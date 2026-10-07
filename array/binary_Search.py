class Solution:
    def binarySearch(self, nums, target) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid
        return -1;

if  __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    target = 5
    c = Solution()
    print(c.binarySearch(arr, target))


