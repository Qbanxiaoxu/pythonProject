#九九乘法表，注意对齐方式。
for i in range(1,10):
    s = ""
    for j in range(1,i+1):
        s+="{1}*{0}={2:<2d} ".format(i, j, i * j)
    print("{:>64}".format(s))