n, m = map(int, input().split())
friend_list = [[] for _ in range(n + 1)]

for _ in range(m):
    f1, f2 = map(int, input().split())
    friend_list[f2].append(f1)
    friend_list[f1].append(f2)


def get_candidates(key: int) -> dict:
    candidates = {}
    s = set(friend_list[key])
    for k, v in enumerate(friend_list):
        if k != key and k not in s and len(v):
            a = len(set(v).intersection(s))
            candidates[k] = a

    return candidates

for candidate in range(1, n + 1):
    test = get_candidates(candidate)
    if len(test) > 0:
        max_val = max(test.values())
        if max_val > 0:
            max_keys = [k for k, v in test.items() if v == max_val]
            result = ' '.join(map(str, max_keys))
            print(result)
        else:
            print(0)
    else:
        print(0)
