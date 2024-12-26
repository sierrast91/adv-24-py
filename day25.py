def get_keys_and_locks(lines):
    locks = []
    keys = []
    is_lock=True
    new=[-1,-1,-1,-1,-1]
    ln= 0
    for line in lines:
        if ln==0 and line=="#####\n":
            is_lock = True
        if ln==6 and line=="#####\n":
            is_lock = False

        if len(line)==1:
            if is_lock:
                locks.append(new)
                print("lock",new)
            if not is_lock:
                keys.append(new)
                print("key",new)
            new=[-1,-1,-1,-1,-1]
            ln=-1
        if len(line)==6:
            for i,ch in enumerate(line[0:5]):
                if ch=="#":
                    new[i]+=1
        ln+=1
    if new!=[-1,-1,-1,-1,-1]:
        if is_lock:
            locks.append(new)
        else:
            keys.append(new)
    print("count:",len(locks),len(keys))
    return locks,keys

def is_pair(lock,key):
    for k,_ in enumerate(lock):
        if lock[k]+key[k]>5:
            return False
    return True
def solve1(lines):
    total=0;
    locks,keys =get_keys_and_locks(lines)
    for lock in locks:
        for key in keys:
            if is_pair(lock,key):
                total+=1
    return total

def solve2(lines):
    return 0;
