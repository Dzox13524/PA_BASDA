import pandas as pd

def Pencarian_fibonacci(data, target):
    n = len(data)

    fib0 = 0
    fib1 = 1
    fibH = fib0 + fib1

    while fibH <= n:
        fib0 = fib1
        fib1 = fibH
        fibH = fib0 + fib1
    batas = -1
    while fibH > 1:
        i = batas + fib0

        if data[i] < target:
            fibH = fib1
            fib1 = fib0
            fib0 = fibH - fib1
            batas = i
        elif data[i] > target:
            fibH = fib0
            fib1 = fib1 - fib0
            fib0 = fibH - fib1
        else:
            return i
        
    if fib1 and batas + 1 < n and data[batas + 1] == target:
        return batas + 1

    return -1
    
data = pd.read_csv("database/Akun.csv")
print(data['Name'].to_list())

