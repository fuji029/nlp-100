# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

import subprocess

def get_lines(path):
    f = open(path, 'r')
    data = f.readlines()
    return data

def execute_unix_command(args):
    return subprocess.run(args=args, stdout=subprocess.PIPE, encoding='utf-8').stdout

def main():
    path = './popular-names.txt'
    doc = get_lines(path)
    print(len(doc))

    print(execute_unix_command(['wc', '-l', path]))

if __name__ == '__main__':
    main()