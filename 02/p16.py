# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys
import subprocess
from p10 import execute_unix_command


def func_py(N, path):
    with open(path, "r") as f:
        lines = f.readlines()
        result = []
        split = ""
        split_line_n = (len(lines) + 1) // N
        for index, line in enumerate(lines):
            split += line
            if ((index + 1) % split_line_n == 0):
                result.append(split)
                split = ""
        if (len(split)):
            result.append(split)
        for i in range(N):
            with open("outputs/16_py_{}".format(i), "w") as f:
                f.writelines(result[i])
        return result


def func_unix(N, path):
    # 3等分なら
    # split -l $(((`wc -l < "popular-names.txt"` + 1)/3)) -d -a 1  popular-names.txt outputs/16_unix_
    args = 'wc -l'.split()
    with open(path, "r") as f:
        n_lines = execute_unix_command(args, stdin=f).replace(" ", "")
    n_lines = (int(n_lines) + 1) // 3
    args = 'split -l {} -d -a {} {} outputs/16_unix_'.format(
        n_lines, len(str(N)), path)
    args = list(args.split())
    execute_unix_command(args)


def main(argv):
    N = int(argv[1])
    path = "./popular-names.txt"

    result_py = func_py(N, path)

    func_unix(N, path)

    for i in range(N):
        with open("./outputs/16_unix_{}".format(i), "r") as f:
            result_unix = f.read()
            if (result_py[i] == result_unix):
                print("test {}: passed✅".format(i))
            else:
                print("test {}: failed❌".format(i))
                exit(-1)
    print("All cases passed✅")


if __name__ == '__main__':
    main(sys.argv)
