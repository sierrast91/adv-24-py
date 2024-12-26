def get_nums(line):
    second = False
    num = 0
    num2 = 0
    for ch in line:
        if ch=='|' or ch =='\n':
            second = True
        elif not second:
            num = num *10 + int(ch)
        elif second:
            num2 = num2 *10 + int(ch)
    return num,num2

def update_order(line,order):
    num,num2 = get_nums(line)
    if num in order:
        order[num].append(num2)
    else:
        order[num] = [num2]

def get_list(line):
    temp = []
    num = 0
    for ch in line:
        if ch=="," or ch=='\n':
            temp.append(num)
            num=0
        else:
            num = num*10 + int(ch)
    return temp

def order_and_list(lines):
    found = False
    order = {}
    l = []
    for line in lines:
        if len(line)==1:
            found = True
        elif not found:
            update_order(line,order)
        elif found:
            l.append(get_list(line))
    return order,l


def isOrdered(t,o):
    if len(t)>=2:
        for i in range(len(t[1:])):
            num = t[i+1]
            arr = t[:i]
            for num2 in arr:
                if o[num].count(num2)!=1:
                    print(num,num2,o[num].count(num2))
                    return False
    return True


def solve1(lines):
    o,l = order_and_list(lines)
    total = 0
    for t in l:
        if isOrdered(t,o):
            total += t[int(len(t)/2)+1]
    return total

def solve2(lines):
    return len(lines)
