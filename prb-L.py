from itertools import permutations

def generate_password_combinations(n):
    # 生成所有可能的數字排列組合
    digits = [str(i) for i in range(1, n+1)]
    perm = permutations(digits)
    
    # 將排列組合轉換為字符串列表並按字典序降序排列
    perm_list = sorted([''.join(p) for p in perm], reverse=True)
    
    return perm_list

# 使用者輸入
n = int(input("請輸入密碼位數 n (2 ≤ n ≤ 9): "))

# 生成並列印密碼組合
password_combinations = generate_password_combinations(n)
for combination in password_combinations:
    print(combination)

