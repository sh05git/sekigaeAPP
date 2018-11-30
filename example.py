import random

members = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# 配列の中からランダムに選択する
print(random.choice(members))

# 配列の中身をシャッフルする
random.shuffle(members)
print(members)

# conn = .connect("")
# cursor = conn.cursor()

# SQL実行
# cursor.execute(sql)
# コミット
# conn.commit()
# 接続を切る
# conn.close()
