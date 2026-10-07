class Solution:
    def sortedArray(self, arr:list[int]) -> list[int]:
        low = 0
        high = len(arr) - 1
        # 定一个新数组接受数据
        result = [float('inf')] * len(arr)
        # 新数组指针
        point = len(result) - 1
        while low <= high:
            if arr[low] ** 2  > arr[high] ** 2:
                result[point] = arr[low] ** 2
                low += 1
                point -= 1
            else:
                result[point] = arr[high] ** 2
                high -= 1
                point -= 1
        return result

if __name__ == "__main__":
    arr = [-10,2,3,4,5,6,7,8,9]
    c = Solution()
    result = c.sortedArray(arr)
    for item in result:

        print(item, end="   ")

