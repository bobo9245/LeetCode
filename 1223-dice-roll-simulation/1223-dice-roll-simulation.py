class Solution:
    def dieSimulator(self, n, rollMax):
        MOD = 10**9 + 7
        dp = [[[0] * 16 for _ in range(6)] for _ in range(n+1)]
        
        # 첫 번째 주사위 던질 때 모든 주사위 숫자별로 1씩 초기화
        for j in range(6):
            dp[1][j][1] = 1
        
        # DP 계산
        for i in range(2, n+1):
            for j in range(6):
                for k in range(1, rollMax[j] + 1):
                    # 이전 주사위에서 다른 숫자를 던졌을 때
                    if k == 1:
                        dp[i][j][k] = sum(sum(dp[i-1][x]) for x in range(6) if x != j) % MOD
                    # 같은 숫자를 던졌을 때 연속해서 k번 나온 경우
                    else:
                        dp[i][j][k] = dp[i-1][j][k-1] % MOD

        # 가능한 모든 시퀀스의 수를 계산
        result = sum(sum(dp[n][j]) for j in range(6)) % MOD
        return result
