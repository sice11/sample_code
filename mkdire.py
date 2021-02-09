import os
import pathlib

new_dir_path = "./sample1/sample2/"

filename = "hoge.txt"

os.makedirs(new_dir_path)

f = pathlib.Path(new_dir_path + "sample.txt")
f.touch()