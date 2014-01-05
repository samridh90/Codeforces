def nextRound():
    n, k = map(int, raw_input().strip().split())
    nums = map(int, raw_input().strip().split())
    if not nums or nums[0] <= 0:
        return 0
    key = nums[k-1]
    if key == 0:
        key += 1
    p = findNextMin(nums, key, 0, n-1)
    if nums[p] == key:
        return len(nums)
    return len(nums[:p])

def findNextMin(nums, k, low, high):
    while low != high:
        mid = (high + low) // 2
        if nums[mid] >= k:
            low = mid + 1
        else:
            high = mid
    return high 

if __name__ == '__main__':
    print nextRound()