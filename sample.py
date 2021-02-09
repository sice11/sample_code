import glob

matchPath = glob.glob("**/sample.txt", recursive=True)

print(matchPath)