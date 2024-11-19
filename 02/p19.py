# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

from p10 import execute_unix_command
import pandas as pd

path = "./popular-names.txt"


def func_py():
    columns = ["Name", "Sex", "Number", "Year"]
    data = []
    with open(path, "r") as f:
        lines = list(f.read().rstrip().split("\n"))
    for line in lines:
        l = list(line.split("\t"))
        l[2] = int(l[2])
        l[3] = int(l[3])
        data.append(l)
    df = pd.DataFrame(data=data, columns=columns)
    name_counts = df["Name"].value_counts()
    name_counts.to_csv("./outputs/19_py.csv", header=False, sep='\t')
    print("Python's result was recorded ./outputs/19_py.csv")
    return


def func_unix():
    args = ["sort col1.txt".split(), "uniq -c".split(),
            ["sort", "-nr",  "-t",  "\t"]]
    out1 = execute_unix_command(args=args[0])
    out2 = execute_unix_command(args=args[1], input=out1)
    with open("outputs/19_unix.csv", "w") as f:
        execute_unix_command(args=args[2], input=out2, stdout=f)
    print("Unix's result was recorded ./outputs/19_unix.csv")
    return


def main():
    func_py()
    func_unix()


if __name__ == '__main__':
    main()
