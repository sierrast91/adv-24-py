
def countXMAS(r,c,lines):
    count = 0
    if not search('X',r,c,lines):
        return count
    if search('M',r,c+1,lines) and search('A',r,c+2,lines)and search('S',r,c+3,lines):
        count+=1
    if search('M',r,c-1,lines) and search('A',r,c-2,lines)and search('S',r,c-3,lines):
        count+=1
    if search('M',r+1,c,lines) and search('A',r+2,c,lines)and search('S',r+3,c,lines):
        count+=1
    if search('M',r-1,c,lines) and search('A',r-2,c,lines)and search('S',r-3,c,lines):
        count+=1
    if search('M',r+1,c+1,lines) and search('A',r+2,c+2,lines)and search('S',r+3,c+3,lines):
        count+=1
    if search('M',r-1,c-1,lines) and search('A',r-2,c-2,lines)and search('S',r-3,c-3,lines):
        count+=1
    if search('M',r+1,c-1,lines) and search('A',r+2,c-2,lines)and search('S',r+3,c-3,lines):
        count+=1
    if search('M',r-1,c+1,lines) and search('A',r-2,c+2,lines)and search('S',r-3,c+3,lines):
        count+=1
    return count
def search(ch,r,c,lines):
    return r>=0 and r<len(lines) and c>=0 and c<len(lines[r]) and ch==lines[r][c]

def searchXMAS(r,c,lines):
    if search('A',r,c,lines):
        if ((search('M',r+1,c+1,lines) and search('S',r-1,c-1,lines)) \
    or (search('S',r+1,c+1,lines) and search('M',r-1,c-1,lines))) \
    and ((search('M',r+1,c-1,lines) and search('S',r-1,c+1,lines)) \
     or (search('S',r+1,c-1,lines) and search('M',r-1,c+1,lines))):
            return True
    return False
def solve1(lines):
    total = 0
    for r,line in enumerate(lines):
        for c,_ in enumerate(line):
            total += countXMAS(r,c,lines)
    return total

def solve2(lines):
    total = 0
    for r,line in enumerate(lines):
        for c,_ in enumerate(line):
            if searchXMAS(r,c,lines):
                total +=1
    return total
