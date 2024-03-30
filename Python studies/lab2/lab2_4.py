def ciąg_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return ciąg_fib(num-2)+ciąg_fib(num-1)

n = int(input("Podaj ile pierwszych wartości ciągu wyświetlić:"))

for i in range(0, n):
    print(ciąg_fib(i), end=" ")
