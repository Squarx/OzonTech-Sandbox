def solution(lst: list):
    tmp = list()
    res = True
    for i in lst:
        if not (i not in tmp or (tmp[-1] == i)):
            res = False
            break
        tmp.append(i)

    if res:
        print("YES")
    else:
        print("NO")


cnt_iter = int(input())
for i in range(cnt_iter):
    cnt = int(input())
    tmp_buff = list(map(int, input().split()))[:cnt]
    solution(tmp_buff)
