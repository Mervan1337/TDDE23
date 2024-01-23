def new_board():
    return {}

def is_free(plan, x, y):
    return (not (x, y) in plan) # Kolla om tupler key finns i plan

def place_piece(plan, x, y, spelare):
    if (is_free(plan,x,y)): #kolla om ledigt
        spelplats = (x, y) #deklarera koordinater
        plan[spelplats] = spelare #lägg koordinater tillsammans med spelarnamn
        return True
    else:
        return False

def get_piece(plan, x, y):
    if not (is_free(plan, x, y)):
        return plan[x, y]
    else:
        return False
def remove_piece(plan, x, y):
    if not (is_free(plan, x, y)):
        del plan[x, y]
        return True
    else:
        return False

def move_piece(plan, gamlax, gamlay, nyax, nyay):
    if not (is_free(plan, gamlax, gamlay)):
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
            if (value == i[0]):
                if(get_piece(plan, value, i[1]) == spelare):
                    counter = counter + 1
        return (counter)
    elif kolumnrad == "row":
        counter = 0
        for i in plan: 
            if (value == i[1]):
                if(get_piece(plan, i[0], value) == spelare):
                    counter += 1
        return (counter)
    else:
        return False

def nearest_piece(plan, x, y):
    if (is_free(plan, x, y)):
        temp_low = None
        temp_low_coordinate = False
        for i in plan:
            xled = i[0]
            yled = i[1]
            distans = ((i[0]-x)**2 + (i[1]-y)**2)**0.5
            if temp_low == None:
                temp_low = distans
            elif (distans <= temp_low):
                temp_low = distans
                temp_low_coordinate = (xled, yled)
        return temp_low_coordinate
    
    else:
        return (x, y)
