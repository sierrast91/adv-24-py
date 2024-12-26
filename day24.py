def get_nodes(lines):
    nodes = {}
    is_gate = False
    for line in lines:
        if len(line)==1:
            is_gate = True
        elif not is_gate:
            key = line[:3]
            val = int(line[5:6])
            nodes[key] = {}
            nodes[key]["val"]=val
        elif is_gate:
            first = line[:3]
            ll = len(line)
            key = line[ll-4:ll-1]
            sec = line[ll-11:ll-8]
            op = line[4:5]
            nodes[key] = {}
            nodes[key]["op"] = op
            nodes[key]["dep"] = [first,sec]
    return nodes

def resolve(key,nodes):
    if not "val" in nodes[key]:
        if nodes[key]["op"]=="A":
            result = resolve(nodes[key]["dep"][1],nodes) & resolve(nodes[key]["dep"][0],nodes)
            nodes[key]["val"]=result
            return nodes[key]["val"]
        elif nodes[key]["op"]=="X":
            result = resolve(nodes[key]["dep"][1],nodes) ^ resolve(nodes[key]["dep"][0],nodes)
            nodes[key]["val"]=result
        elif nodes[key]["op"]=="O":
            result = resolve(nodes[key]["dep"][1],nodes) | resolve(nodes[key]["dep"][0],nodes)
            nodes[key]["val"]=result
    return nodes[key]["val"]
    
def solve1(lines):
    nodes = get_nodes(lines)
    for node in nodes:
        if not "val" in nodes[node]:
            resolve(node,nodes)
    return get_num(nodes)
def get_num(nodes):
    i=0
    num = 0
    while(True):
        key = f"z{i:02}"
        print(key)
        if not key in nodes:
            break
        num = num |nodes[key]["val"]<<i
        i+=1
    return num

def solve2(lines):
    return 0
