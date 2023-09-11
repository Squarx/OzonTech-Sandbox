buff = list(list())

cnt = int(input())
for i in range(0, cnt):
    cnt_workers = int(input())
    tmp_buff = list(map(int, input().split()))
    tmp_buff = tmp_buff[0:cnt_workers]
    buff.append(tmp_buff)


def solution(workers: dict):
    for id, skill in workers.items():
        tmp = {id_i: abs(skill - sk_i) for id_i, sk_i in workers.items() if id_i != id}
        min_value = min(tmp.values())
        min_key = next(key for key, value in tmp.items() if value == min_value)
        print(id, min_key)
        workers.pop(id)
        workers.pop(min_key)
        solution(workers)
        return


for b in buff:
    workers = dict(zip([i for i in range(1, len(b) + 1)], b))
    solution(workers)
    if b != buff[-1]:
        print()
