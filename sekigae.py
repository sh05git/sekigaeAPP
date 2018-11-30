import random


def main():
    with open("member_list", mode="r")as f:
        # split 文字列を分割する
        members = f.read().split("\n")
        # メンバーをランダムに並べ替える(今回のメンバーは15人)
    random.shuffle(members)

    # 並べ替えたメンバーを3つのテーブルに分ける(テーブルAは6人、Bは5人、Cは4人)
    # ', '.joinとすることで、リストの[]を外して、リストの中身を', 'で結合できる)
    print(f"テーブルAのメンバーは{', '.join(members[:6])}です。")
    print(f"テーブルBのメンバーは{', '.join(members[6:11])}です。")
    print(f"テーブルCのメンバーは{', '.join(members[11:])}です。")

    # print(f"テーブルAのメンバーは{', '.join(members[:6])}\nBのメンバーは{', '.join(members[6:11])}\nCのメンバーは{', '.join(members[11:])}です。")


if __name__ == '__main__':
    main()
