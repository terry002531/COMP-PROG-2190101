def reverse(d):
    new = {}
    for k, v in d.items():
        new[v] = k
    return new

def keys(d, v):
    result = []
    for k in d:
        if d[k] == v:
            result.append(k)
    return result

exec(input().strip())