# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#   - 英小文字ならば(219 - 文字コード)の文字に置換
#   - その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(s):
    dst = ""
    for char in s:
        if char.islower():
            dst += chr(219 - ord(char))
        else:
            dst += char
    return dst

def main():
    message = "Hello, my name is Yuki Fujiwara!"
    encoded = cipher(message)
    print(encoded)
    decoded = cipher(encoded)
    print(decoded)

if __name__ == '__main__':
    main()
