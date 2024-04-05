def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)
    # 初始化一个(n+1)长度的数组，i位置存储以nums[i]结尾的最长递增子序列的长度
    dp = [1] * (n + 1)

    # 动态规划填充dp数组
    for i in range(1, n + 1):
        for j in range(i):
            if nums[i - 1] > nums[j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)

    # dp数组中的最大值即为最长递增子序列的长度
    return max(dp)



# 如果需要输出最长递增子序列本身，可以稍作修改，增加额外的逻辑来记录路径
def longest_increasing_subsequence_with_seq(nums):
    n = len(nums)
    dp = [1] * (n + 1)
    parent = [-1] * n  # 记录构成当前LIS的前一个元素索引

    for i in range(1, n + 1):
        for j in range(i):
            if nums[i - 1] > nums[j - 1]:
                if dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i - 1] = j - 1

    # 反向查找最长递增子序列
    lis = []
    idx = dp.index(max(dp))
    while idx != -1:
        lis.append(nums[idx])
        idx = parent[idx]
    lis.reverse()

    return lis


if __name__ == '__main__':
    # 示例：
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    lis_length = longest_increasing_subsequence(nums)
    print(f"最长递增子序列的长度是：{lis_length}")

    lis_sequence = longest_increasing_subsequence_with_seq(nums)
    print(f"最长递增子序列是：{lis_sequence}")
