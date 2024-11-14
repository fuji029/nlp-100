# 11. タブをスペースに変換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

from p10 import execute_unix_command

def func_py(path):
    f = open(path, 'r')
    data = f.read()
    
    data = data.replace("\t", " ")
    
    return data

def func_unix(path):
    args = ["sed", "s/\t/ /g", path]
    return execute_unix_command(args=args)


def main():
    path = "./popular-names.txt"

    if(func_py(path) == func_unix(path)):
        print("Successed")    
    else:
        print("Failed")

if __name__ == '__main__':
    main()
