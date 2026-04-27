import math

class Rational:
    def __init__(self, a, b=None):
        if b is None:
            if isinstance(a, Rational):
                self.n, self.d = a.n, a.d
            else:
                p = a.split('/')
                self.n, self.d = int(p[0]), int(p[1])
        else:
            self.n, self.d = a, b
        self.s()

    def s(self):
        g = math.gcd(self.n, self.d)
        self.n //= g
        self.d //= g
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

    def __add__(self, o):
        if isinstance(o, int): o = Rational(o, 1)
        return Rational(self.n * o.d + o.n * self.d, self.d * o.d)

    def __sub__(self, o):
        if isinstance(o, int): o = Rational(o, 1)
        return Rational(self.n * o.d - o.n * self.d, self.d * o.d)

    def __mul__(self, o):
        if isinstance(o, int): o = Rational(o, 1)
        return Rational(self.n * o.n, self.d * o.d)

    def __truediv__(self, o):
        if isinstance(o, int): o = Rational(o, 1)
        if o.n == 0: raise ZeroDivisionError
        return Rational(self.n * o.d, self.d * o.n)

    def __call__(self):
        return self.n / self.d

    def __getitem__(self, k):
        if k == "n": return self.n
        if k == "d": return self.d

    def __setitem__(self, k, v):
        if k == "n": self.n = v
        elif k == "d": self.d = v
        self.s()

    def __repr__(self):
        return f"{self.n}/{self.d}"

def e(v):
    t = v.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
    r = Rational(t[0], 1) if '/' not in t[0] else Rational(t[0])
    i = 1
    while i < len(t):
        o = t[i]
        n = t[i+1]
        x = Rational(n, 1) if '/' not in n else Rational(n)
        if o == '+': r = r + x
        elif o == '-': r = r - x
        elif o == '*': r = r * x
        elif o == '/': r = r / x
        i += 2
    return r

with open("C:\\Users\\User\\Desktop\\input01.txt", "r") as f:
    for l in f:
        l = l.strip()
        if l:
            try:
                res = e(l)
                print(f"Result: {res} ({res()})")
            except Exception as m:
                print(f"Error: {m}")