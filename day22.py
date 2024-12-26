CONST_MOD = 16777216

def mix(secret,num):
    return secret ^ num
def prune(secret):
    return secret%CONST_MOD


def evolve(secret):
    secret =mix(64*secret,secret)
    secret =prune(secret)
    secret =mix(int(secret/32),secret)
    secret =prune(secret)
    secret = mix(2048*secret,secret)
    secret = prune(secret)
    return secret

def secret_from_lines(lines):
    secret=[]
    for line in lines:
        secret.append(int(line[:-1]))
    return secret
def solve1(lines):
    secrets = secret_from_lines(lines)

    for i,_ in enumerate(secrets):
        for _ in range(2000):
            secrets[i] = evolve(secrets[i])

    return sum(secrets)

def get_prices(lines):
    secrets = secret_from_lines(lines)
    p = {}
    for i,s in enumerate(secrets):
        p[i] = [s%10]
    for i,_ in enumerate(secrets):
        for _ in range(2000):
            secrets[i] = evolve(secrets[i])
            p[i].append(secrets[i]%10)
    return p
def solve2(lines):
    prices = get_prices(lines)
    for p in prices:
        print(p,prices[p])
    return 0
