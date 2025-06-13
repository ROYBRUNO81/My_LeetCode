def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    pal = s[0]
    l = 1
    # DP table
    n = len(s)
    dp = [[False]*n for _ in range(n)]

    # Base case
    for i in range(n):
        dp[i][i] = True
        if i+1 < n:
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                pal = s[i:i+2]
                l = 2

    for k in range(2, n):
        i = 0
        for j in range(k, n):
            if (s[i] == s[j]) and dp[i+1][j-1]:
                dp[i][j] = True
                if j - i + 1 > l:
                    pal = s[i:j+1]
                    l = j - i + 1
            i += 1
            if i == n-k:
                break

    return pal

print(longestPalindrome("caba"))