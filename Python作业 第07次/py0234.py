#表格打印,编写一个名为 printTable()的函数，它接受字符串的列表，将它显示在组织良好的表格中，如下所示。假定所有内层列表都包含同样数目的字符串。
def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j])>colWidths[i]:
                colWidths[i]=len(tableData[i][j])
    #print(colWidths)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if i==0:
                tableData[i][j]=tableData[i][j].rjust(colWidths[i])
            else:
                tableData[i][j] = tableData[i][j].ljust(colWidths[i])
    #print(tableData)
    for i in range(len(tableData)):
        print("{0:<} {1:>} {2:>}".format(tableData[0][i],tableData[1][i],tableData[2][i]))

tableData = [	['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']	]
printTable(tableData)