import os

path="C:/vscode/100days/clutter"
os.chdir(path)
files=os.listdir()
y=1
for i in files:
    if i.endswith(".png"):
        os.rename(f"{i}", f"{y}.png")
    y+=1
print(os.getcwd())