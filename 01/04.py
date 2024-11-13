#04. 元素記号
#“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

def main():
    s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    s = list(s.split())
    index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    my_dict = {}
    for i, word in enumerate(s):
        if((i+1) in index):
            word = word[0]
        else:
            word = word[:2]
        my_dict[str(i+1)] = word
    print(my_dict)

if __name__ == "__main__":
    main()