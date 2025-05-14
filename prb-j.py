'''
1.理解問題描述：
    接受一個正整數 n, 並重複以下步驟直到n 變成 1：
        如果 n 是偶數，就將它除以 2；
        如果 n 是奇數，就將它乘以 3 再加 1。
    最後輸出所有經過演算法產生的數值。

2.分析輸入和輸出格式：
    輸入是一個正整數 n。
    輸出是經過演算法產生的所有數值，按照順序輸出成一行，以空格隔開。

3.設計演算法：
    使用一個循環來重複上述步驟，直到n 變成 1。
    在每一步中，根據n 的奇偶性質，來決定下一個數值。
    將每一步產生的數值存入一個列表中。

4.實現程式碼：
    定義一個函數 simulate_algorithm(n) 來執行上述演算法。
    使用一個循環來重複步驟，並將每一步的數值存入列表。
    最後輸出列表中的所有數值。
'''
"""定義函數 simulate_algorithm(n)：這個函數接受一個正整數 n 作為參數。
    初始化列表 sequence這個列表, 用來存儲演算法過程中產生的所有數值。"""
def simulate_algorithm(n):
    sequence = []
    """循環 while n != 1： 這個循環會一直執行，直到 n 變成 1。
        添加數值到列表 sequence.append(n)：在每次循環中，將當前的 n 添加到 sequence 列表中。"""
    while n != 1:
        sequence.append(n)
        """判斷 n 的奇偶性：
            如果 n 是偶數 (n % 2 == 0)，則將 n 除以 2 (n = n // 2)。
            如果 n 是奇數 (else)，則將 n 乘以 3 再加 1 (n = n * 3 + 1)。"""
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    """添加數值 1 到列表 sequence.append(1), 當 n 變成 1 時，將 1 添加到 sequence 列表中。
    返回列表 return sequence, 返回包含所有數值的 sequence 列表。"""
    sequence.append(1)
    return sequence

# 自行輸入
n = int(input("請輸入一個正整數: "))

# 獲取數值順序
sequence = simulate_algorithm(n)

# 輸出數值順序
print(" ".join(map(str, sequence)))
