class MatrixPython:
    rows: int
    cols: int
    matrix: list[list[int]]
    sort_list: list[int]
    last_col_sort: int

    def __init__(self, rows, cols, matrix_out: list[list[int]], cols_to_sort):
        self.rows = rows
        self.cols = cols
        self.matrix = matrix_out
        self.sort_list = cols_to_sort
        self.last_col_sort = -1

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(str(val) for val in row) + "\n"
        return matrix_str

    def sort(self):
        for col in self.sort_list:
            if col == self.last_col_sort:
                continue
            tmp = [self.matrix[val][col] for val in range(len(self.matrix))]

            start_dict = dict(zip([i for i in range(len(self.matrix))], tmp))
            tmp.sort()
            new_order = list()
            for i in tmp:
                f_key = None
                for key, value in start_dict.items():
                    if value == i:
                        f_key = key
                        break

                new_order.append(f_key)
                start_dict.pop(f_key)
            self.matrix = [self.matrix[i] for i in new_order]
            self.last_col_sort = col
def input_4():
    rows, cols = map(int, input().split())
    i = 0
    matrix_in = list(list())
    while i < rows:
        tmp_buff = list(map(int, input().split()))
        tmp_buff = [tmp_buff[i] for i in range(cols)]
        matrix_in.append(tmp_buff)
        i += 1
    cnt_sort = int(input())
    tmp_buff = list(map(int, input().split()))
    tmp_buff = [tmp_buff[i] - 1 for i in range(cnt_sort)]
    buff_cols = list()
    buff_cols = [val for val in tmp_buff if val not in buff_cols]
    return rows, cols, matrix_in, buff_cols

row: int
col: int
iterations = int(input())

for i in range(iterations):
    trash = input()
    row, col, matrix, cols_to_sort = input_4()
    m = MatrixPython(row, col, matrix, cols_to_sort)
    m.sort()
    print(m)

