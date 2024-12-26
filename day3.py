def get_enabled(line,i,enabled):
    if enabled and line[i]=='d' and line[i+1]=='o' and line[i+2]=='n' and line[i+3]=='\''and line[i+4]=='t' and line[i+5]=='(' and line[i+6]==')':
        return not enabled
    if not enabled and line[i]=='d' and line[i+1]=='o'and line[i+2]=='('and line[i+3]==')':
        return not enabled
    return enabled

def get_num(line,index):
    num = 0
    while is_digit(line[index]):
        num = num *10 + int(line[index])
        index+=1
    return index,num
def is_digit(ch):
    digits = "0123456789"
    for d in digits:
        if d==ch:
           return True
    return False

def get_mult(line,index):
    if line[index]!='m':
        return 0
    if line[index+1]!='u':
        return 0
    if line[index+2]!='l':
        return 0
    if line[index+3]!='(':
        return 0
    ni,num = get_num(line,index+4)
    if ni== index+4:
        return 0
    if line[ni]!=',':
        return 0
    ni2,num2 = get_num(line,ni+1)
    if ni2 == ni+1:
        return 0
    if line[ni2]!=')':
        return 0
    return num*num2

def solve1(lines):
    total = 0
    for line in lines:
        for i,_ in enumerate(line):
            num= get_mult(line,i)
            total += num
    return total

def solve2(lines):
    total = 0
    enabled = True
    for line in lines:
        for i,_ in enumerate(line):
            if line[i]=='d':
                enabled = get_enabled(line,i,enabled)
            num = get_mult(line,i)
            if enabled:
                total+=num
    return total
