# with open("example.txt", "w") as file:
#     file.write("mshia")


# with open("example.txt", "r") as f:
#     content = f.read()
#     print(content)
# print(len(content))


# with open("example.txt", "a") as f:
#     f.write(" sad aris uaxloesi sacxobi")


with open("example.txt", "r",encoding="utf-8") as f:
    content = f.read()
with open("example1.txt", "w",encoding="utf-8") as f1:
    f1.write(content)