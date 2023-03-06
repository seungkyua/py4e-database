fname = input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:
    pieces = line.split()
    for piece in pieces:
        if piece in lst:
            continue
        else:
            lst.append(piece)
lst.sort()
print(lst)