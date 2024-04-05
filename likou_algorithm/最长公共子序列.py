def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    # 初始化一个(m+1) * (n+1)的矩阵，记录每个位置的LCS长度
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # 动态规划填充表格
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 根据dp矩阵从右下角反向追溯得到最长公共子序列
    lcs = ''
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs, dp[m][n]

if __name__ == '__main__':

    # 示例：
    s1 = "ABCBDAB"
    s2 = "BDCAB"
    lcs_str, lcs_length = longest_common_subsequence(s1, s2)
    print(f"最长公共子序列是：{lcs_str}")
    print(f"最长公共子序列的长度是：{lcs_length}")