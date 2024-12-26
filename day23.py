def conn_list(lines):
    conn = {}
    for line in lines:
        first =line[:2]
        second = line[3:5]
        if first in conn:
            if not second in conn[first]:
                conn[first][second]=1
        if not first in conn:
            conn[first] = {}
            conn[first][second]=1
        if second in conn:
            if not first in conn[second]:
                conn[second][first]=1
        if not second in conn:
            conn[second] = {}
            conn[second][first]=1
    return conn

def get_trios(conn):
    trio = []
    for st in conn:
        st_friend = conn[st]
        for nd in st_friend:
            nd_friend = conn[nd]
            for rd in nd_friend:
                if rd in st_friend:
                    trio.append([st,nd,rd])
    return trio

def solve1(lines):
    conn = conn_list(lines)
    total=0
    trios = get_trios(conn)
    for trio in trios:
        if trio[0][0]=='t' or trio[1][0]=='t' or trio[2][0]=='t':
            total+=1
    return total/6


def all_friends(user,conn,lan):
    for fr in lan:
        if not fr in conn[user]:
            return False
    return True

def recursive_lan(conn,lans):
    mylans = lans.copy()
    for user in conn:
        for i,lan in enumerate(lans):
            if all_friends(user,conn,lan):
                mylans[i].append(user)
                mylans = recursive_lan(conn,mylans)

        mylans.append([user])
        mylans = recursive_lan(conn,mylans)
        print(mylans)
    return mylans
        
def solve2(lines):
    conn = conn_list(lines)
    lans = []
    lans = recursive_lan(conn,lans)
    return 0
