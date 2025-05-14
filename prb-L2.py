def generate_password_combinations(n):
        # 輔助函數來生成排列組合
    def permute(digits, path, result):
        if not digits:
            result.append(path)
            return
        for i in range(len(digits)):
            permute(digits[:i] + digits[i+1:], path + digits[i], result)
    
    # 生成從 1 到 n 的所有可能的數字排列組合

    digits = [str(i) for i in range(1, n+1)]
    result = []
    permute(digits, '', result)
    
    # 結果按字典序降序排列
    result.sort(reverse=True)
    
    return result

# 使用者輸入
n = int(input("請輸入密碼位數 n (2 ≤ n ≤ 9): "))

# 生成並列印密碼組合
password_combinations = generate_password_combinations(n)
for combination in password_combinations:
    print(combination)
