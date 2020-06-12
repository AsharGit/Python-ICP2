d = {}
file = open("test.txt")
data = file.read()
words = data.split()

for i in words:
    d[i] = d.get(i, 0) + 1

print(d)
file.close()

