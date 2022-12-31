mults=[[0 for j in range(9)] for i in range(9)]

for i in range(9):
    for j in range(9):
        mults[i][j] = (i+1)*(j+1)

for i in range(9):
    for j in range(9):
        print("%3d"%(mults[i][j]), end="")
    print()
