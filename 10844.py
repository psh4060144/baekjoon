# 쉬운 계단수

def dp(x):
    global lst
    if x == 1:
        return
    tmp_lst = [0] * 10
    for i in range(10):
        if i - 1 < 0:
            j = 0
        else:
            j = lst[i - 1]
        if i + 1 >= 10:
            k = 0
        else:
            k = lst[i + 1]

        tmp_lst[i] = j + k
    lst = tmp_lst
    return dp(x - 1)


lst = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
N = int(input())
dp(N)
print(sum(lst) % 1000000000)
