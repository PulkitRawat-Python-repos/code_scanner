import logic_01
mat = []
for i in range(4):
    mat.append([0]*4) # creation of a 4*4 matrix with all its elements as zero
print("'u' : up") 
print("'d' : down") 
print("'r' : right") 
print("'l' : left") 
logic_01.addNew_tile(mat)
print(mat)
while(True):
    x = input("press the command ")
    if (x == "l"):
        mat= logic_01.move_left(mat) 
        status = logic_01.status(mat) # used everytime since we have to check for everystep
        print(status)
        if (status == "game continues"):
            logic_01.addNew_tile(mat)
        else:
            break
    elif (x == "r"): #if-elif ladder or multiple if statements anything can be used
        mat = logic_01.move_right(mat)
        status = logic_01.status(mat)
        print(status)
        if (status == "game continues"):
            logic_01.addNew_tile(mat)
        else:
            break
    elif (x == "d"):
        mat = logic_01.move_down(mat)
        status = logic_01.status(mat)
        print(status)
        if (status == "game continues"):
            logic_01.addNew_tile(mat)
        else:
            break
    elif (x == "u"):
        mat = logic_01.move_up(mat)
        status = logic_01.status(mat)
        print(status)
        if (status == "game continues"):
            logic_01.addNew_tile(mat)
        else:
            break
    else:
        print("error")
    print(mat)

