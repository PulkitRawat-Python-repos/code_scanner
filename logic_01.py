import random
def addNew_tile(mat):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while (mat[r][c]!=0):
        r = random.randint(0,3)
        c = random.randint(0,3)
    mat[r][c]=2
    return mat
def status(mat):
    for i in range(4): # any tile scores 2048
        for j in range(4):
            if(mat[i][j] == 2048):
                return "victorious"
    for i in range(4): # any tile is left empty
        for j in range(4):
            if(mat[i][j] == 0):
                return "game continues"
    for i in range(3): # any merging ocurring
        for j in range(3):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "game continues"
    for i in range(3):
        if(mat[i][3] == mat[i+1][3]):
            return "game continues"
    for j in range(3):
        if(mat[3][j] == mat[3][j+1]):
            return "game continues"
    return "lost"
def stack(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        p=0 # it rep the cell where the non zero value will move
        for j in range(4):
            if (mat[i][j]!=0): # when the number in the matrix is non-zero it will move back to previous empty cell  
                new_mat[i][p]=mat[i][j]
                p+=1
    mat = new_mat # if the cell is zero the cell will either be occupied or remain as it is
    return new_mat
    # doesn't bring change in original matrix
def merge(mat):
    for i in range(4): 
        for j in range(3):
            while (mat[i][j] == mat[i][j+1] and mat[i][j]!=0):
                mat[i][j] = 2*mat[i][j]
                mat[i][j+1] = 0
    return mat
    # brings change in original matrix 
    # has to be applied 3 times 
def reverse(mat):
    new_mat = [] # intro of new matrix since here change in matrix cannot happen cpp way
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j]) 
    return new_mat
# doesn't bring change in original matrix
def transpose(mat):
    new_mat = [] 
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i]) 
    return new_mat
# doesn't bring change in original matrix
def move_left(mat):
    a= stack(mat)
    for i in range(3): # to be performed as many times as the index of the matrix is
        for j in range(3):
            (merge(a))
        a = stack(a)
    return a
def move_right(mat):
    c = reverse(mat)
    d = move_left(c)
    e = reverse(d)
    return e
def move_up(mat):
    c = transpose(mat)
    d= move_left(c)
    e = transpose(d)
    return e
def move_down(mat):
    c = transpose(mat)
    d= move_right(c)
    e = transpose(d)
    return e

mat = [[8,4,2,2],[8,0,0,2],[2,0,0,2],[16,0,0,16]]
print(move_down(mat))
# print(stack(mat))
# a= stack(mat)
# for i in range(3):
#     (merge(a))
# print(a)
# b = stack(a)
# return b

                

