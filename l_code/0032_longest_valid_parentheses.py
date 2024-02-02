def longest_valid_parentheses(s):
    max_len = 0

    stack = [-1]

    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


def longest_valid_parentheses_dp(s):
    n = len(s)
    max_len = 0

    # dp[i] is the longest valid parentheses ending at s[i - 1]
    dp = [0] * n

    for i in range(1, n):
        if s[i] == '(':
            continue

        if s[i - 1] == '(':
            prefix_length = dp[i - 2] if i-2 >= 0 else 0
            dp[i] = prefix_length + 2
        elif s[i - 1] == ')':
            length = dp[i - 1]
            if length == 0:
                continue

            if i - length - 1 >= 0 and s[i - length - 1] == '(':
                prefix_length = dp[i - length - 2] if i - length - 2 >= 0 else 0
                dp[i] = dp[i - 1] + 2 + prefix_length
        max_len = max(max_len, dp[i])

    return max_len


def test():
    assert longest_valid_parentheses_dp("()(())") == 6



