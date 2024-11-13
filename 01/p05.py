#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

def n_gram(s, n):
    return [s[i:i+n] for i in range(len(s) - n + 1)]

def main():
    s = "I am an NLPer"

    word_bi_gram = n_gram(list(s.split()), 2)
    print("単語bi-gram : ", word_bi_gram)

    letter_bi_gram = n_gram(s.replace(" ", ""), 2)
    print("文字bi-gram : ", letter_bi_gram)

if __name__ == '__main__':
    main()
