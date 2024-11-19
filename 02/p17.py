# 17. 1列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはcut, sort, uniqコマンドを用いよ．

from p10 import execute_unix_command

path = "./popular-names.txt"


def func_py():
    with open(path, "r") as f:
        data = f.read().split("\n")
    rows = []
    for item in data:
        l = list(item.split("\t"))
        rows.append(l[0])
    col1_set = set(rows)
    return col1_set


def func_unix():
    args = ["cut -f 1 {}".format(path).split(), "sort", "uniq"]
    out1 = execute_unix_command(args[0])
    out2 = execute_unix_command(args[1], input=out1)
    out3 = execute_unix_command(args[2], input=out2)
    return set(list(out3.split("\n")))


def main():
    result_py = func_py()
    result_unix = func_unix()

    if (result_py == result_unix):
        print("test passed✅")
        with open("outputs/17_set.txt", "w") as f:
            f.writelines("\n".join(list(result_py)))
        print("The result was recorded outputs/17_set.txt")
    else:
        print("error❌")
        exit(-1)


if __name__ == "__main__":
    main()
