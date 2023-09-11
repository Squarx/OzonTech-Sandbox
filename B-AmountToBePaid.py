from collections import Counter

cnt_input = int(input())


def get_sum(d):
    summa = 0
    for k, v in d.items():
        triple, ost = divmod(v, 3)
        summa += triple * 2 * k + ost * k
    return summa


for i in range(0, cnt_input):
    cnt = int(input())
    tmp_buff = list(map(int, input().split()))
    tmp_buff = [tmp_buff[i] for i in range(cnt)]
    d = Counter(tmp_buff)
    print(get_sum(d))
