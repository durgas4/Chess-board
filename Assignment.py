#three functions defining the moves for bishop, knight and invalid moves
#presentin the grid
#defined board length M
#board breadth breadth N
#determined the valid steps x,y for bishop
#determined the valid steps for m,n in knight

from itertools import product
from itertools import chain


#valid moves for knight
def knight_moves(x,y):
    #X=[]
    #key_knight=[]
    #x, y = coord
    #M,N=size
    #move={}
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < M and y < N ]
    #X.append[moves]
    return moves


#valid moves for bishop
def bishop_moves(x,y):
    #key_bishop=[]
    if x<N and y<M :
            return list(chain(
        [(x, y)],
        zip(range(x - 1, -1, -1), range(y - 1, -1, -1)),
        zip(range(x + 1, M, 1), range(y + 1, N, 1)),
        zip(range(x + 1, M, 1), range(y - 1, -1, -1)),
        zip(range(x - 1, -1, -1), range(y + 1, N, 1))))
    #else:
        
            

def invalid_moves(x,y):
    #x,y=0,0
    moves=[]
    for moves in (x,y):
        moves =[(2,0),(0,3),(0,7),(2,6),(4,3),(6,7),(7,1)]
        #list(product[2,0])+list(product[0,3])+list(product[0,7])+list(product[2,6])+list(product[4,3])+list(product[6,7])+list(product[7,1])
        #(,[0,3],,[,,,)#tuples immutable
        return moves
    
    
    
    
#print('Invalid moves',invalid_moves(x,y))

def apply(x,y):
    queue=[]
    # loop until we have one element in queue
    while(len(queue) > 0):
         
        t = queue[0]
        queue.pop(0)
         
        # if current cell is equal to target
        # cell, return its distance
        if(t.x == x[0] and
           t.y == y[0]):
            return t.dist
             
        # iterate for all reachable states
        for i in range(N):
            for j in range(M):
                x = t.x + bishop_moves(i,j)
                y = t.y + knight_moves(i,j)
                queue.append(cell(x, y))
                
def main_prog(n):
    Knight=knight_moves(x,y)
    Bishop=bishop_moves(m,n)
    In=invalid_moves(x,y)
    for Knight in Bishop:
        if Knight not in In and Bishop not in In:
            if Knight is not None:
                if Bishop is not None:
                    apply(Knight,Bishop)# this part is throwing error when co-ordinates of Knight and bishop is more than board dimension
                    #any suggestions would be great
                    print(1)
                else:
                    print('Move out of board dimension') 

if __name__ == '__main__':
    M=int(input('length'))
    N=int(input('breadth'))
    x=int(input('Enter x position for knight'))
    y=int(input('Enter y position for knight'))
    #Knight=knight_moves(x,y)
    
    #print('valid moves \n',)
    #In=invalid_moves(x,y)
    #print('invalid moves',)
    m=int(input('\n Enter x position for Bishop'))
    n=int(input('Enter y position for Bishop'))
    #Bishop=bishop_moves(m,n)
    
    #Valid_knight= x.Knight-In
    #Valid_Bishop=Bishop-In
    #print('valid moves',)
    main_prog(n)

        
            
            
        
        
        


    






