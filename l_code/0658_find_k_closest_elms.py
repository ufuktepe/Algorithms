# O(log(N) + k)
def find_k_closest(arr, k, x):
    left = 0
    right = len(arr) - 1

    # O(log(N))
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    # O(k)
    count = 0
    i = right
    j = right + 1
    start_idx = None
    while count < k:
        low = high = None
        if 0 <= i < len(arr):
            low = arr[i]
        if 0 <= j < len(arr):
            high = arr[j]

        if low is None:
            if start_idx is None: start_idx = j
            j += 1
        elif high is None:
            start_idx = i
            i -= 1
        elif abs(x - low) <= abs(x - high):
            start_idx = i
            i -= 1
        else:
            if start_idx is None: start_idx = j
            j += 1

        count += 1

    # O(k)
    count = 0
    res = []
    while count < k:
        res.append(arr[start_idx + count])
        count += 1
    return res


# O(log(N) + k)
def find_k_closest_v2(arr, k, x):
    left = 0
    right = len(arr) - 1

    # O(log(N))
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    # Find the index of the closest element
    if right == -1:
        i = 0
    elif right == len(arr) - 1:
        i = right
    else:
        i = right if abs(arr[right] - x) <= abs(arr[left] - x) else left

    # O(k)
    count = 1  # element at index i must be in the result. Hence, we start the count at 1.
    j = i + 1  # j - 1 will be the last element included in the result.
    while count < k:
        if i == 0:
            j += 1
        elif j == len(arr) or abs(arr[i - 1] - x) <= abs(arr[j] - x):
            i -= 1
        else:
            j += 1


        count += 1

    return arr[i:j]

def find_k_closest_v3(arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left+k]

def test_1():
    arr = [1, 2, 3, 4, 5, 6]
    x = 4
    k = 3
    assert find_k_closest_v3(arr, k, x) == [3, 4, 5]
    x = 9
    k = 2
    assert find_k_closest_v3(arr, k, x) == [5, 6]
    x = 0
    k = 1
    assert find_k_closest_v3(arr, k, x) == [1]