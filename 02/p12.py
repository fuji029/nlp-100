# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

from p10 import execute_unix_command


def func_py(path):
    f = open(path, 'r')
    rows = f.readlines()
    cols = [[] for _ in range(2)]
    for row in rows:
        row = list(row.split('\t'))
        cols[0].append(row[0])
        cols[1].append(row[1])

    f = open('./outputs/col1.txt', 'w')
    f.write("\n".join(cols[0]) + "\n")

    f = open('./outputs/col2.txt', 'w')
    f.write("\n".join(cols[1]) + "\n")


def func_unix(path):
    arg1 = ['cut', '-f', '1', path]
    arg2 = ['cut', '-f', '2', path]
    return execute_unix_command(arg1), execute_unix_command(arg2)


def main():
    path = './popular-names.txt'
    func_py(path)

    test1, test2 = func_unix(path)

    f = open("col1.txt", "r")
    data = f.read()
    if (data != test1):
        print("Failed : col1.txt")
        return

    f = open("col2.txt", "r")
    data = f.read()
    if (data != test2):
        print("Failed : col2.txt")
        return

    print("Successed")


if __name__ == '__main__':
    main()
