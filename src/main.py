import sys

#change with ur path
sys.path.insert(0, 'C:/Users/ASUS/15-Puzzle-Solver/src')
import os
import time
import preprogress
import Solver

final = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

os.chdir("./TestCase")
file = input("Masukkan nama file: ")

f = open(file,"r")


puzzle = []
for item in f:
    arr = (item.strip("\n").split(" ")[:4])
    arr2 = []
    for i in arr:
        idx = int(i)
        arr2.append(idx)
    puzzle.append(arr2)
f.close()

#print kurang(i)
preprogress.printKurang(puzzle)

#print sigmakurang
sigmakurang = preprogress.isReachableGoal(puzzle)
print("SigmaKurang(i):",sigmakurang)

#is reachable goal?
if(sigmakurang%2 == 1):
    print("puzzle tidak solveable")
else:
    start = time.time()
    Solver.solve(puzzle,preprogress.emptyTile(puzzle),final)
    end = time.time()
    print("Execution time: ",end-start)