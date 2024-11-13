#06. 集合
#“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．

from p05 import n_gram

def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"

    X = set(n_gram(s1, 2))
    Y = set(n_gram(s2, 2))

    print("X = ", X)
    print("Y = ", Y)

    union = X | Y
    intersection = X & Y
    difference = X - Y

    print("union : ", union)
    print("intersection : ", intersection)
    print("difference : ", difference)

    print("Is 'se' in X? : " + ("Yes" if 'se' in X else "No"))
    print("Is 'se' in Y? : " + ("Yes" if 'se' in Y else "No"))

if __name__ == '__main__':
    main()