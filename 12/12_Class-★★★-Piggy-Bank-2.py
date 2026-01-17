class piggybank:
    def __init__(self):
        self.coins = {}

    def add(self, v, n):
        if v not in self.coins:
            if n >= 100:
                return False
            else:
                self.coins[v] = n
                return True
        else:
            if self.coins[v] + n >= 100:
                return False
            else:
                self.coins[v] += n
                return True

    def __float__(self):
        s = 0.0
        if self.coins == {}:
            return s
        else:
            for k, v in self.coins.items():
                s += float(v) * float(k)
            return s

    def __str__(self):
        result_items = []
        for key in sorted(self.coins.keys()):
            result_items.append(f"{key}:{self.coins[key]}")
        return "{" + ", ".join(result_items) + "}"

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank()
p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)