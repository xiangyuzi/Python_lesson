#変数fruitsに複数の文字列を要素に持つリストを代入
fruits = ["apple", "banana", "orange"]

#インデックス番号0を出力
print(fruits[0])

#インデックス番号2の要素を文字列と連結して出力
print("好きな果物は"+fruits[2]+"です")

#リストの末尾に文字列grapeを追加
fruits.append("grape")
print(fruits)

#インデックス番号0の要素を文字列cherryに更新
fruits[0] = "cherry"
print(fruits[0])