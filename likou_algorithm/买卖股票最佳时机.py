from typing import List


class Solution:
    """
    这段代码中，dp[i][j][0]表示在第i天，已经持有股票并且还剩下j次卖出机会的最大收益，
    dp[i][j][1]则表示同一天不持有股票的情况下，剩下的买卖机会。
    通过比较前一天持有股票继续持有的收益和卖出股票然后再次买入的收益，我们可以更新每一天的状态。最后返回的就是最优解。
    """
    def maxProfit(self, prices: List[int], k: int) -> int:
        if not prices or k <= 0:
            return 0

        n = len(prices)

        # 定义状态转移方程
        # dp[i][k][0] 表示在第i天，已经持有股票并且还剩下k次卖出机会可以获得的最大利润
        # dp[i][k][1] 表示在第i天，未持有股票并且还剩下k次买卖机会可以获得的最大利润
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]

        # 初始化状态，第0天不能卖出股票，所以卖出利润都为0
        for i in range(k + 1):
            dp[0][i][0] = -prices[0]
            dp[0][i][1] = 0

        # 动态规划计算
        for i in range(1, n):
            for j in range(1, k + 1):
                # 已持有股票的情况
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] - prices[i])
                # 未持有股票的情况
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] + prices[i])

        # 返回最后一次不持有股票并且用尽所有买卖机会时的最大利润
        return dp[n - 1][k][1]
