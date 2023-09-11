class s21_date:
    h: int
    m: int
    s: int
    all: int

    def __init__(self, date: str):
        l = date.split(sep=':')
        self.h = int(l[0])
        self.m = int(l[1])
        self.s = int(l[2])
        self.all = self.s + self.m * 60 + self.h * 60 * 60

    def validate(self) -> bool:
        return (0 <= self.h <= 23) and (0 <= self.m <= 59) and (0 <= self.s <= 59)




cnt_iter = int(input())
for it in range(cnt_iter):
    all_sec = set(range(23 * 60 * 60 + 59 * 60 + 59 + 1))
    cnt_date = int(input())
    flag = False
    for i in range(cnt_date):
        date = input().split(sep='-')
        if flag:
            continue
        d1 = s21_date(date[0])
        d2 = s21_date(date[1])
        if not d1.validate() or not d2.validate() or d1.all > d2.all:
            flag = True

        if flag:
            continue

        s = set(range(d1.all, d2.all + 1))

        if len(all_sec.intersection(s)) != len(s):
            flag = not flag
        else:
            all_sec.difference_update(s)
        if flag:
            continue

    if flag:
        print("NO")
    else:
        print("YES")
