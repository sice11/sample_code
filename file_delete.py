import glob
import os
import datetime as dt


# 変数の定義

# ログファイルのタイトルの変数
now = dt.datetime.now()
time = now.strftime("%Y%m%d")


# 削除対象のファイルリスト
file_list = [
    "a.txt",
    "b.txt",
    "c.txt",
]




# ファイル削除実行部分
for file in file_list:
    with open("./log/{}.log".format(time), "a") as f:
        f.write(file + "\n")
    matchPath = glob.glob("**/{}".format(file), recursive=True)
    # matchPathはリストで取得される
    if len(matchPath) == 0:
        not_file = "{}は見つかりませんでした。\n".format(file)
        with open("./log/{}.log".format(time), "a") as f:
            f.write(not_file)
    else:
        os.remove(matchPath[0])
        delete_file = "delete>>" + matchPath[0] + "\n"
        with open("./log/{}.log".format(time), "a") as f:
            f.write(delete_file)
