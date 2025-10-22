
s = [
    [9],
    [12, 15],
    [10, 6, 8],
    [2, 18, 9, 5],
    [19, 7, 10, 4, 16],
]

# state: (score, [value...])
dp = []
for i in range(len(s)):
    temp = []
    for j in range(len(s[i])):
        if i == len(s) - 1:
            temp.append((s[i][j], [s[i][j]]))
        else:
            temp.append((0, []))
    dp.append(temp)

for i in range(len(s) - 2, -1, -1):
    for j in range(len(s[i])):
        if dp[i + 1][j][0] > dp[i + 1][j + 1][0]:
            dp[i][j] = (dp[i + 1][j][0] + s[i][j], dp[i + 1][j][1] + [s[i][j]])
        else:
            dp[i][j] = (dp[i + 1][j + 1][0] + s[i][j], dp[i + 1][j + 1][1] + [s[i][j]])


score, values = dp[0][0]
print(score)
print(list(reversed(values)))
