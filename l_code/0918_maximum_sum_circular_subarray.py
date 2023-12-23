def max_sum(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    overall_max = float('-inf')

    for i in range(n):
        cur_max = nums[i]
        overall_max = max(overall_max, cur_max)

        for j in range(1, n):
            k = (j + i) % n
            cur_max = max(cur_max + nums[k], nums[k])
            overall_max = max(overall_max, cur_max)

    return overall_max


def max_sum(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    cur_min = 0
    overall_min = float('inf')
    min_idx = 0

    for i in range(n):
        cur_min = min(cur_min + nums[i], nums[i])
        if cur_min < overall_min:
            overall_min = cur_min
            min_idx = i

    # print(overall_min)
    # print(min_idx)
    cur_max = 0
    overall_max = float('-inf')

    for j in range(n):
        k = (j + min_idx + 1) % n
        if nums[k] > cur_max + nums[k]:
            print(f'start: {k}')
        else:
            print(f'mid: {k}')
        cur_max = max(cur_max + nums[k], nums[k])
        if cur_max > overall_max:
            print(f'end {k}')
        overall_max = max(overall_max, cur_max)


    return overall_max


def maxSubarraySumCircular(nums):
    if len(nums) == 1:
        return nums[0]

    # minimum = minimum middle array
    # maximum = maximum array if the problem weren't circular
    minimum = maximum = total = cur_max = cur_min = nums[0]
    start = end = start_local = 0
    for i, n in enumerate(nums[1:]):
        # keep track of total array sum
        total += n

        # keep track of current minimum subarray and maximum
        # this is just kadane from the previous problem adjusted a bit because now we have negative numbers
        cur_min = min(cur_min + n, n)
        if cur_max + n < n:
            start = i + 1
            end = i + 1
        else:
            end = i + 1
        cur_max = max(cur_max + n, n)

        # update the global min and max
        minimum = min(cur_min, minimum)

        if cur_max > maximum:
            print(f'start: {start} end: {end}')
            maximum = max(cur_max, maximum)
            print(f'maximum: {maximum}')

    # The entire array is the minimum sum, so a better circular cannot exist.
    # Simply return the best subarray if the problem weren't circular
    if minimum == total:
        return maximum

    print(f'maximum: {maximum}')
    print(f'minimum: {minimum}')
    print(f'total: {total}')
    print(f'total - minimum: {total - minimum}')


    # The greatest subarray may be circular, or it may not me
    # Return the max of the best non-circular and circular subarray
    return max(maximum, total - minimum)

def asd():
    nums = [88,-35,50,-38,-60,-31,-2,-8,-8,91,-14,50,-25,-26,1,71,-91,-64,-40,46,30,-97,9,-55,-36,-75,71,99,90,-53,-68,-20,-73,89,-14,74,-8,72,82,48,45,2,-42,12,77,22,87,56,73,-21,78,15,-6,-75,24,46,-11,-70,-90,-77,57,43,-66,10,-30,-47,91,-37,-4,-67,-88,19,66,29,86,97,-4,67,54,-92,-54,71,-42,-17,57,-91,-9,-15,-26,56,-57,-58,-72,91,-55,35,-20,29,51,70]
    print(maxSubarraySumCircular(nums))

asd()