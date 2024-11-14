# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

import sys
from p10 import execute_unix_command

def func_py(n, path):
    with open(path, "r") as f:
        data = "".join(f.readlines()[:n])
    return data

def func_unix(n, path):
    args = ["head", "-{}".format(n), path]
    return execute_unix_command(args)

def main(argv):
    n = int(argv[1])
    path = "popular-names.txt"

    data_py = func_py(n, path)
    data_unix = func_unix(n, path)

    print("Python:")
    print(data_py)

    print("Unix:")
    print(data_unix)

    if(data_py == data_unix):
        print("Successed")
    else:
        print("Failed")

if __name__ == "__main__":
    main(sys.argv)