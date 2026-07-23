from solution import is_valid_sudoku

def blank():
    return [["."] * 9 for _ in range(9)]

def main():
    b = blank()
    if not is_valid_sudoku(b):
        raise AssertionError("empty")
    b[0][0] = b[0][1] = "5"
    if is_valid_sudoku(b):
        raise AssertionError("row dup")
    b = blank()
    b[0][0] = b[1][0] = "5"
    if is_valid_sudoku(b):
        raise AssertionError("col dup")
    b = blank()
    b[0][0] = b[1][1] = "5"
    if is_valid_sudoku(b):
        raise AssertionError("block dup")
    b = blank()
    b[0][0] = "1"
    b[0][8] = "2"
    b[8][0] = "3"
    if not is_valid_sudoku(b):
        raise AssertionError("ok partial")
    print("OK")

if __name__ == "__main__":
    main()
