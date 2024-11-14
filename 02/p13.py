# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，
# 元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

from p10 import execute_unix_command

def func_py(path):
    with open("col1.txt", "r") as f:
        cols1 = f.readlines()
    with open("col2.txt", "r") as f:
        cols2 = f.readlines()
    
    with open(path, "w") as f:
        for col1, col2 in zip(cols1, cols2):
            f.write(col1[:-1] + "\t" + col2[:-1] + "\n")

def func_unix():
    args = ["paste", "col1.txt", "col2.txt"]
    return execute_unix_command(args)

def main():
    path = "popular-names13.txt"
    func_py(path)

    test = func_unix()
    with open(path, "r") as f:
        if(f.read() == test):
            print("Successed")
        else:
            print("Failed")

if __name__ == '__main__':
    main()
