# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
import subprocess


# Unixコマンドを実行
def execute_unix_command(args: list, stdin=None, input=None, stdout=subprocess.PIPE):
    return subprocess.run(args=args, stdin=stdin, input=input, stdout=stdout, encoding='utf-8').stdout


def main():
    path = './popular-names.txt'
    with open(path, 'r') as f:
        lines = f.readlines()
    print("Python:", len(lines))

    # Unix : wc -l < popular-names.txt

    # 引数
    args = "wc -l".split()
    # 入力ファイル
    f = open(path, "r")
    print("Unix:", execute_unix_command(args=args, stdin=f))


if __name__ == '__main__':
    main()
