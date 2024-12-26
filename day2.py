
def toArrays(lines):
    list = []
    for line in lines:
        temp = []
        for num in line.split():
            temp.append(int(num))
        list.append(temp)
    return list

def isSafe(line):
    prev = None
    pdif = 0
    for cur in line:
        if prev!=None:
            dif = cur-prev
            if dif==0 or dif < -3 or dif>3:
                return False
            if pdif*dif<0:
                return False
            pdif = dif
        prev = cur
    return True

def check(cur,prev):
    if cur==prev:
        return False
def isSafe2(line):
    for i in range(len(line)):
        t = line[:i]+line[i+1:]
        print(t,line)
        if isSafe(t):
            return True
    return False
def solve1(lines):
    list = toArrays(lines)
    cnt = 0
    for t in list:
        if isSafe(t):
            cnt+=1
    return cnt
def solve2(lines):
    list = toArrays(lines)
    cnt = 0
    for t in list:
        if isSafe(t):
            cnt+=1
        elif isSafe2(t):
            cnt+=1
    return cnt
