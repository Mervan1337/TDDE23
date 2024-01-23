# args = arguments, par = parameter
def interpret(args, par):
    if not isinstance(args, list):
        if args in par:
            return par[args]
        else:
            return args
    # List length is 2
    elif len(args) == 2:
        if args[0] in par and args[1] not in par:
            return par[args[0]]
        elif args[0] == "NOT":
            if not isinstance(args[1], list):
                if args[1] in par:
                    if par[args[1]] == "true":
                        return "false"
                    else:
                        return "true"
            elif interpret(args[1], par) == "true":
                return "false"
            else:
                return "true"
    # List length is 3                    
    elif len(args) == 3:
        if args[1] == "AND":
            if interpret(args[0], par) == "true" and interpret(args[2], par) == "true":
                return "true"
            else:
                return "false"
        # OR statement
        else:
            if interpret(args[0], par) == "true" or interpret(args[2], par) == "true":
                return "true"
            else:
                return "false"
          
def split_rec(indata):
    word_left = ""
    word_right = ""
    if not indata:
        return word_left, word_right
    word_left, word_right = split_rec(indata[1:]) 
    if indata[0].islower() or indata[0] == "_" or indata[0] == ".":
        word_left = indata[0] + word_left
    elif indata[0].isupper() or indata[0] == "|" or indata[0] == " ":
        word_right = indata[0] + word_right
    return word_left, word_right

def split_it(indata, word_left = "", word_right = ""):
    for c in indata:
        if c.islower() or c == "_" or c == ".":
            word_left += c
        if c.isupper() or c == "|" or c == " ":
            word_right += c
    return word_left, word_right
        