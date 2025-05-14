def round_to_two_decimal_places(x):
    rounded_value = round(x + 1e-9, 2)  # 加上一個微小的值以確保正確的四捨五入
    if rounded_value == -0.00:
        rounded_value = 0.00
    return rounded_value

# 讀取測試資料的數量
n = int(input("請輸入測試資料的數量: "))

# 初始化列表來存儲結果
results = []

# 讀取每個測試資料並進行四捨五入
for _ in range(n):
    x = float(input())
    results.append(round_to_two_decimal_places(x))

# 輸出結果
for result in results:
    print(f"{result:.2f}")


