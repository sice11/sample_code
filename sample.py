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
    print(matchPath[0])

    os.remove(matchPath[0])
