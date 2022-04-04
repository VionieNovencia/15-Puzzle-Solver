#mengisi matrix puzzle dengan inputan user
def getPuzzle():
    puzzle = [list(map(int,input().split())) for i in range(4)] 
    return puzzle

#16 = ubin kosong

#menghitung nilai fungsi kurang(i) dari ubin i
def kurang(puzzle,i,j ):
    count = 0
    ubin = i*4 + j+1
    for u in range(4):
        for v in range(4):
            ubin2 = u*4 + v+1
            if(puzzle[u][v] < puzzle[i][j] and ubin2>ubin):
                count+=1
    return count

def printKurang(puzzle):
    array = [0 for i in range(17)]
    for p in range(4):
        for q in range(4):
            array[puzzle[p][q]] = kurang(puzzle,p,q)
    for i in range(1,17):
        print("Kurang("+ str(i)+ ") =", array[i])
            
#hitung kurang(i)+X
def isReachableGoal(puzzle):
    sum = 0
    X = -1
    for i in range(4):
        for j in range(4):
            if (puzzle[i][j] == 16):
                X = (i+j)%2
            sum += kurang(puzzle,i,j)
    if (X != -1):
        sum += X
        return sum
    else:
        return -1

#mendapatkan tile yang kosong
def emptyTile(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                return [i,j]
