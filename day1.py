
def toArrays(lines):
    arr1=[]
    arr2=[]
    for line in lines:
        num1,num2 = line.split()
        num1 = int(num1)
        num2 = int(num2)
        arr1.append(num1)
        arr2.append(num2)
    return arr1,arr2


def add(cur,val):
    if val<0:
        return cur-val
    else:
        return cur+val
def solve1(lines):
    arr1,arr2 = toArrays(lines)
    arr1.sort()
    arr2.sort()
    total = 0
    for i in range(len(arr1)):
        total = add(total,arr1[i-1]-arr2[i-1])
    return total


def solve2(lines):
    arr1,arr2 = toArrays(lines)
    total = 0
    mem = {}
    for num1 in arr1:
        if not num1 in mem:
            temp = 0
            for num2 in arr2:
                if num1 == num2:
                    temp = temp + 1
            mem[num1]= temp * num1
        total = total+ mem[num1]
    return total

