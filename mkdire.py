import os
import pathlib

new_dir_path = "./sample1/sample2/"

# 作成するファイル一覧
make_files = [
    "a.txt",
    "b.txt",
    "c.txt",
]

# 新規でフォルダ階層を作成
os.makedirs(new_dir_path)

# 新規で作成したディレクトリ最下部に対象のファイルを配置
for make_file in make_files:
    f = pathlib.Path(new_dir_path + make_file)
    f.touch()