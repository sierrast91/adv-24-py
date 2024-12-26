# NUMPAD
#   +---+---+---+
#   | 7 | 8 | 9 |
#   +---+---+---+
#   | 4 | 5 | 6 |
#   +---+---+---+
#   | 1 | 2 | 3 |
#   +---+---+---+
#       | 0 | A |
#       +---+---+

def numpad_aim(ch):
    if ch=='A':
        return 2,0
    elif ch=='0':
        return 1,0
    else:
        return (int(ch)%3)-1,(int(ch)+2)//3

# KEYPAD
#       +---+---+
#       | ^ | A |
#   +---+---+---+
#   | < | v | > |
#   +---+---+---+

def keypad_aim(ch):
    if ch=='^':
        return 1,1
    elif ch=='A':
        return 2,1
    elif ch=='<':
        return 0,1
    elif ch=='v':
        return 1,0
    else: # '>'
        return 2,0
def numpad_on(px,py):
    if px==2 and py==0: return "A"
    elif px==1 and py==0: return "0"
    elif px==0 and py==1: return "1"
    elif px==1 and py==1: return "2"
    elif px==2 and py==1: return "3"
    elif px==0 and py==2: return "4"
    elif px==1 and py==2: return "5"
    elif px==2 and py==2: return "6"
    elif px==0 and py==3: return "7"
    elif px==1 and py==3: return "8"
    elif px==2 and py==3: return "9"
    else :print("error:",px,py)
def keypad_on(px,py):
    if px==2 and py==1:return "A"
    elif px==1 and py==1:return "^"
    elif px==0 and py==0:return ">"
    elif px==1 and py==0:return "v"
    elif px==2 and py==0:return ">"
    else: print("error:",px,py)

def numpad_go(cmd):
    px=2
    py=0
    str=""
    for ch in cmd:
        print(ch,px,py)
        if ch=='A': str = str + f"{numpad_on(px,py)}"
        elif ch=='<': px-=1
        elif ch=='>': px+=1
        elif ch=='v': py-=1
        elif ch=='^': py+=1
    return str

def keypad_go(cmd):
    px=2
    py=1
    str=""
    for ch in cmd:
        if ch=='A': str = str + f"{keypad_on(px,py)}"
        elif ch=='<': px-=1
        elif ch=='>': px+=1
        elif ch=='v': py-=1
        elif ch=='^': py+=1


def numpad_solve(cmd):
    str = ""
    px = 2
    py = 0
    for ch in cmd:
        ax,ay = numpad_aim(ch)
        while px!=ax or py!=ay:
            if ay>py:
                str+="^"
                py+=1
            elif ax<px:
                str+="<"
                px-=1
            elif ax>px:
                str+=">"
                px+=1
            elif ay<py:
                str+="v"
                py-=1
        str+="A"
    return str
def keypad_solve(cmd):
    str=""
    py=1
    px=2
    for ch in cmd:
        ax,ay = keypad_aim(ch)
        while px!=ax or py!=ay:
            if ay<py:
                str+="v"
                py-=1
            elif ax>px:
                str+=">"
                px+=1
            elif ax<px:
                str+="<"
                px-=1
            elif ay>py:
                str+="^"
                py+=1
        str+="A"
    return str

def solve1(lines):
    lines=["029A\n","980A\n","179A\n","456A\n","379A\n"]
    total = 0
    for cmd in lines:
        str=numpad_solve(cmd[:-1])
        print(f"output {cmd[:-1]}:",str,numpad_go(str))
        # str = keypad_solve(str)
        # print(str,keypad_go(str))
        # str = keypad_solve(str)
        # print(str,keypad_go(str))
        total += int(cmd[:-2])*len(str)
    return total


def solve2(lines):
    return 0
