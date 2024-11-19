# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

import subprocess


def get_lines(path):
    f = open(path, 'r')
    data = f.readlines()
    return data


def execute_unix_command(args, stdin=None, input=None, stdout=subprocess.PIPE):
    return subprocess.run(args=args, stdin=stdin, input=input, stdout=stdout, encoding='utf-8').stdout


def main():
    path = './popular-names.txt'
    doc = get_lines(path)
    print("Python", len(doc))

    print("Unix:", execute_unix_command(['wc', '-l', path]))


if __name__ == '__main__':
    main()
