import glob
import os

file_list = [
    "a.txt",
    "b.txt",
    "c.txt",
]


for file in file_list:
    print(file)
    matchPath = glob.glob("**/{}".format(file), recursive=True)
    # matchPathはリストで取得される
    if len(matchPath) == 0:
        print("{}は見つかりませんでした。".format(file))
    else:
        os.remove(matchPath[0])
        print("delete >> " + matchPath[0])