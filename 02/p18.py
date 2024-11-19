# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

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
    df.sort_values(by="Number", ascending=False, inplace=True)
    df.to_csv("./outputs/18_py.csv", sep="\t", header=False, index=False)
    print("Python's result was recorded ./outputs/18_py.csv")
    return df


def func_unix():
    args = ["sort", "-nr",  "-t",  "\t",  "-k",  "3", path]
    with open("./outputs/18_unix.csv", "w") as f:
        execute_unix_command(args=args, stdout=f)
    print("Unix's result was recorded ./outputs/18_unix.csv")


def main():
    func_py()
    func_unix()


if __name__ == '__main__':
    main()
