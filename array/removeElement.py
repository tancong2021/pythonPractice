class Solution(object):
    def removeElement(self, arr, target) -> int:
        slow, fast = 0, 0
        size = len(arr)
        while fast < size:
            if arr[fast] == target:
                arr[slow] = arr[fast]
                slow += 1
                size -= 1
            fast += 1
        return size;

if __name__ == "__main__":
    arr = [1,2,3,3,3,3,7,8,9]
    target = 3
    c = Solution()
    print(c.removeElement(arr, target))