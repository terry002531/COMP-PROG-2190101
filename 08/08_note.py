for k, v in d.items():  # d.items() 返回形如 (key, value)
    pass                # [3:"A"]  ->  key = 3 ; value = "A"


mp = {}
for _ in range(n):
     first, nick = input().split()
     mp[first] = nick   # 正向：真名 -> 昵称
     mp[nick]  = first  # 反向：昵称 -> 真名
                        # 建立映射列表 mp
print(mp.get(q, "Not found"))
                        # 从映射表 mp 中找 q 对应的名字或昵称；如果没有，输出 ‘Not found’


sorted_items = sorted(num.items(), key=lambda x: (-x[1], x[0]))
                        # 把 num.items() 得到的 (字符, 次数) 对，按“次数降序、字符升序”的规则排序
                        # num[a] = 2 ; num.items() -> ('a', 2)
                        # lambda x: (-x[1], x[0])，把每个二元组 x=(字母, 次数) 映射为 (-次数, 字母)
                        # ('a', 2) -> (-2, 'a')
                        # Python 对元组做字典序比较：先比第 1 个元素（这里是 -次数），相等时再比第 2 个元素（这里是 字母）


key = f'{a} {b}' # 拼接字符a，b，中间是“ ”
key = f'{a}-{b}' # 拼接字符a，b，中间是“-”


rev = {str(v): k for k, v in mp.items()}
                        # 反向映射：交换 mp 的key，value，给 rev

s = " ".join(out)       # 将数组 out 中所有元素按顺序拼接，以“ ”间隔
s = " ".join(out[::-1]) # 从最后一个到第一个拼接