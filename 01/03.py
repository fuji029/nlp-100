#03. 円周率
#“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

def main():
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    s = s.replace(",", "")
    s = s.replace(".", "")
    words = list(s.split())
    l = [len(word) for word in words]
    print(l)
    pi = str(l[0]) + "." + "".join([str(length) for length in l[1::] ])
    print(pi)

if __name__ == "__main__":
    main()