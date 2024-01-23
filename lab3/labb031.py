def new_board():
    return {}

def is_free(plan, x, y):
    return not (x, y) in plan # Kolla om tupler key finns i plan

def place_piece(plan, x, y, spelare):
    if is_free(plan,x,y): #kolla om ledigt
        spelplats = (x, y) #deklarera koordinater
        plan[spelplats] = spelare #lägg koordinater tillsammans med spelarnamn
        return True
    else:
        return False

def get_piece(plan, x, y):
    if not is_free(plan, x, y):
        return plan[x, y]
    else:
        return False
def remove_piece(plan, x, y):
    if not is_free(plan, x, y):
        del plan[x, y]
        return True
    else:
        return False

def move_piece(plan, gamlax, gamlay, nyax, nyay):
    if not is_free(plan, gamlax, gamlay):
        spelare = get_piece(plan, gamlax, gamlay)
        remove_piece(plan, gamlax, gamlay)
        place_piece(plan, nyax, nyay, spelare)
        return True
    else:
        return False
        

def count(plan, kolumnrad, value, spelare):
    if kolumnrad == "column":
        counter = 0
        for i in plan: 
            # i[0] = x, i[1] = y
            if value == i[0]:
                if get_piece(plan, value, i[1]) == spelare:
                    counter = counter + 1
        return counter
    elif kolumnrad == "row":
        counter = 0
        for i in plan: 
            if value == i[1]:
                if(get_piece(plan, i[0], value) == spelare):
                    counter += 1
        return counter
    else:
        return False

def nearest_piece(plan, x, y):
    if is_free(plan, x, y):
        lowest = None
        lowest_coordinate = False
        for i in plan:
            xled = i[0]
            yled = i[1]
            distans = ((i[0]-x)**2 + (i[1]-y)**2)**0.5
            if lowest == None:
                lowest = distans
            elif distans <= lowest:
                lowest = distans
                lowest_coordinate = (xled, yled)
        return lowest_coordinate
    
    else:
        return (x, y)


def choose(n,k):
    if k == n or k == 0:
        return 1
    elif k > (n-k):
        return perm(n,k)//factorial(n-k)
    else:
        return perm(n,n-k)//factorial(k)
def factorial(n):
    if n == 1:
        return n
    else: 
        return n * factorial(n-1)
def perm(n,k):
    if n == k:
        return (1)
    else: 
        return n * perm(n-1,k)


board = new_board()
#print(is_free(board, 500, 100))
place_piece(board, 500, 100, "spelare1")
place_piece(board, 1, 100, "spelare2")
place_piece(board, 500, 100, "spelare2")
place_piece(board, 500, 200, "spelare2")
is_free(board, 500, 100)
get_piece(board, 500, 100)
get_piece(board, 666,666)
remove_piece(board, 500, 100)
remove_piece(board, 1, 1)
is_free(board, 500, 100)
move_piece(board,  500, 200, 500, 100)
get_piece(board, 500, 100)
print(count(board, "column", 500, "spelare2"))
count(board, "row", 100, "spelare2")
nearest_piece(board, 500, 105)
#print(is_free(board, 500, 100))
#print(get_piece(board, 500, 100))
#print(remove_piece(board, 500, 100))
#print(is_free(board, 500, 100))
#print (move_piece(board, 500, 100, 800, 600))
#print (is_free(board, 500, 100))
#print (is_free(board, 800, 600))
#print (get_piece(board, 800, 600))
#print (count(board, "column", 500, "spelare2"))
#print(nearest_piece(board, 500, 111))
