mp = {
    'a':2 , 'b':22 , 'c':222,
    'd':3 , 'e':33 , 'f':333,
    'g':4 , 'h':44 , 'i':444,
    'j':5 , 'k':55 , 'l':555,
    'm':6 , 'n':66 , 'o':666,
    'p':7 , 'q':77 , 'r':777 , 's':7777,
    't':8 , 'u':88 , 'v':888,
    'w':9 , 'x':99 , 'y':999 ,
    'z':9999 , ' ':0
}

# 反向映射：'2' -> 'a', '22' -> 'b', ...
rev = {str(v): k for k, v in mp.items()}

def text2keys(text):
    text = text.lower()
    out = []
    for ch in text:
        if ch in mp:                 # 忽略非英文字母
            out.append(str(mp[ch]))  # 注意转成字符串，便于 join
    s = " ".join(out)
    return s

def keys2text(keys):
    tokens = keys.split()            # 以空格分组："666","66","6",...
    out = []
    for t in tokens:
        if t in rev:                 # 忽略非法段
            out.append(rev[t])
    return "".join(out)

exec(input().strip())