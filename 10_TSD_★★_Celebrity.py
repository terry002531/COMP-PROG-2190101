def knows(R,x,y):
    if y in R[x]:
        return True
    else:
        return False

def is_celeb(R,x):
    for i in R:
        if i != x and knows(R,x,i):
            pass
        else:
            return False
    return True

def find_celeb(R):
    for person in R:
        if is_celeb(R, person):
            return person
    return None

def read_relations():
    R = {}
    while True:
        d = input().strip()
        if d == 'q' or len(d) == 1:
            break
        c,e = d.split(' ')
        if c in R:
            R[c].append(e)
        else:
            R[c] = [e]
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print("Not Found")
    else:
        print(c)

exec(input().strip())