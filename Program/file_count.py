d = {}

# Read file to get data
file = open('test.txt', 'r')
data = file.read()
words = data.split()
file.close()

# Add word and count to dictionary
for i in words:
    d[i] = d.get(i, 0) + 1

# Write dictionary to file
file = open('test.txt', 'a')
file.write('\n')
file.write(str(d))
file.close()

