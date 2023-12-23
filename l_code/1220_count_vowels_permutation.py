# Time: O(n)  Space: O(n)
def count_vowel_permutations(n):
    vowels = ['a', 'e', 'i', 'o', 'u']

    # dp[i][j] is the num of vowels of length i that ends with letter vowels[j]
    dp = [[0] * 5 for _ in range(n + 1)]

    # Base cases
    for j in range(len(vowels)):
        dp[1][j] = 1

    for i in range(2, n + 1):
        for j in range(len(vowels)):
            if j == 0:
                # 'a'
                dp[i][j] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]

            elif j == 1:
                # 'e'
                dp[i][j] = dp[i - 1][0] + dp[i - 1][2]

            elif j == 2:
                # 'i'
                dp[i][j] = dp[i - 1][1] + dp[i - 1][3]

            elif j == 3:
                # 'o'
                dp[i][j] = dp[i - 1][2]

            elif j == 4:
                # 'u'
                dp[i][j] = dp[i - 1][2] + dp[i - 1][3]

    return sum(dp[-1]) % (10 ** 9 + 7)


def test():
    assert count_vowel_permutations(1) == 5
    assert count_vowel_permutations(2) == 10
    assert count_vowel_permutations(5) == 68