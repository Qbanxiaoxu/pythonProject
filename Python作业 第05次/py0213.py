# 1、从键盘输入n，然后输出n行的杨辉三角形。
# 要求：
# 1)  n的大小不限制
# 2)  必须用列表推导式创建二维数组
# 3)  用循环产生数组中的数据
n=int(input("n="))
matrix=[[0 for j in range(i+1)] for i in range(n)]
for i in range(n):
    if i==0:
        matrix[i][i]=1
    elif i==1:
        matrix[i][0]=1
        matrix[i][i]=1
    else:
        for j  in range(i+1):
            if j==0 or j==i:
                matrix[i][j] = 1
            else:
                matrix[i][j]=matrix[i-1][j]+matrix[i-1][j-1]
print(matrix)
input("Press enter to end")