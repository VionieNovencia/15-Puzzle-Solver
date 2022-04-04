from asyncio.windows_events import NULL
import copy
from heapq import heappush, heappop
 
#Class priorityqueue
class priorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, k):
        heappush(self.heap, k)

    def pop(self):
        return heappop(self.heap)
 
    def isEmpty(self):
        if not self.heap:
            return True
        else:
            return False
#class node
class node:
     
    def __init__(self, parent,puz, empty_tile_pos,
                 cost, level,direction):
                      
        self.parent = parent
 
        self.puz = puz
 
        self.empty_tile_pos = empty_tile_pos
 
        self.cost = cost
 
        self.level = level

        self.direction = direction
 
    def __lt__(self, nxt):
        return self.cost < nxt.cost

#menghitung cost simpul
def calculateCost(puz, final,level) -> int:
     
    count = level
    for i in range(4):
        for j in range(4):
            if (puz[i][j] and puz[i][j] != final[i][j]):
                count += 1
                 
    return count

#membuat node baru
def newNode(mat, empty_tile_pos, new_empty_tile_pos,
            level, parent, final,direction) -> node:
                 
    new_mat = copy.deepcopy(mat)
 
    x1 = empty_tile_pos[0]
    y1 = empty_tile_pos[1]
    x2 = new_empty_tile_pos[0]
    y2 = new_empty_tile_pos[1]
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
 
    cost = calculateCost(new_mat, final,level)
 
    new_node = node(parent, new_mat, new_empty_tile_pos,
                    cost, level,direction)
    return new_node

#mencetak jawaban dari akar ke daun
def printTree(root):
     
    if root == None:
        return
     
    printTree(root.parent)
    printMatrix(root.puz)
    print()

#print matrix
def printMatrix(mat):
     
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 16):
                print("\033[91m{}\033[00m".format(str(mat[i][j])), end = "  ")
            elif(mat[i][j] < 10):
                print(mat[i][j], end = "  ")
            else:
                print(mat[i][j], end = " ")

             
        print()


def isValid(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

#empty slot baru
def new_empty(empty_tile,dir):
    new = [-1,-1]
    if (dir == "left"):
        new[0] = empty_tile[0]
        new[1] = empty_tile[1]-1
    elif(dir == "right"):
        new[0] = empty_tile[0]
        new[1] = empty_tile[1]+1
    elif(dir == "up"):
        new[0] = empty_tile[0]-1
        new[1] = empty_tile[1]
    elif(dir == "down"):
        new[0] = empty_tile[0]+1
        new[1] = empty_tile[1]
    return new

#memeriksa apakah puzzle = final
def isEqual(puzzle,final):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] != final[i][j]):
                return False
    return True

def solve(initial, empty_tile_pos, final):
    count = 0

    pq = priorityQueue()
 
    cost = calculateCost(initial, final,0)
    root = node(None, initial,
                empty_tile_pos, cost, 0, NULL)
    pq.push(root)
    while not pq.isEmpty():
 
        minimum = pq.pop()
        #memeriksa apakah sudah sesuai dengan final
        if isEqual(minimum.puz,final):
            printTree(minimum)
            print("Banyak anak dibangkitkan:" , count) 
            return

        #menentukan arah direction baru agar tidak looping
        if minimum.direction == NULL:
            directions = ["left","right","up","down"]
        elif minimum.direction == "left":
            directions = ["left","up","down"]
        elif minimum.direction == "right":
            directions = ["right","up","down"]
        elif minimum.direction == "up":
            directions = ["left","right","up"]
        elif minimum.direction == "down":
            directions = ["left","right","down"]

        for i in range(len(directions)):
            new_tile_pos = new_empty(minimum.empty_tile_pos,directions[i])
                
            if isValid(new_tile_pos[0], new_tile_pos[1]):
                
                #buat node baru
                new_node = newNode(minimum.puz,
                                minimum.empty_tile_pos,
                                new_tile_pos,
                                minimum.level + 1,
                                minimum, final, directions[i])
                #masukkan node baru ke prioqueue
                pq.push(new_node)
                count += 1
                