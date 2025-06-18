import os

# ファイルの読み(r)と書き込み(r"+")
with open('myfile.txt', 'r+', encoding='utf-8') as f:
    data = f.read()
    print(f"{len(data)}")
    # print(f"{data}:{len(data)}")

