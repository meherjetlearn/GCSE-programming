arr = [1, 3, 5, 7, 9, 11, 13]
target = 555
left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        print(f"Element {target} found at index {mid}.")
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("not found")