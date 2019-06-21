tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    i = 0
    while i < len(tableData):
        colWidths[i] = len(max(tableData[i], key=len))
        i = i + 1
    for x in range(len(tableData[0])):
        for y in range(len(colWidths)):
            print(tableData[y][x].rjust(colWidths[y]), end=' ')
        print(end='\n')
printTable(tableData)