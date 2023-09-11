from itertools import zip_longest


def all_same(items: (tuple, list, str)) -> bool:
    return all(item == items[0] for item in items)


def common_suffix(strings: (list, tuple), _min: int = 0, _max: int = 100) -> str:
    if strings[0] == strings[1]:
        return ''
    suffix = ""
    strings = [string[::-1] for string in strings]
    for tup in zip_longest(*strings):
        if all_same(tup):
            suffix += tup[0]
        else:
            break

    suffix = suffix[::-1]

    if _min <= len(suffix) <= _max:
        return suffix
    return ''


cnt_dict = int(input())
words_dict = [input() for _ in range(cnt_dict)]

cnt_w = int(input())

words_rifm = []
for _ in range(cnt_w):
    word = input()
    max_id = max(range(len(words_dict)), key=lambda id: len(common_suffix([words_dict[id], word])))
    print(words_dict[max_id])
