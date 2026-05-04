import math

class Rational:
    def __init__(self, a, b=None):
        if b is None:
            if isinstance(a, Rational):
                self.n, self.d = a.n, a.d
            else:
                p = str(a).split('/')
                if len(p) == 2:
                    self.n, self.d = int(p[0]), int(p[1])
                else:
                    self.n, self.d = int(p[0]), 1
        else:
            self.n, self.d = int(a), int(b)
        self.s()

    def s(self):
        g = math.gcd(abs(self.n), abs(self.d))
        self.n //= g
        self.d //= g
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d

    def __add__(self, o):
        if isinstance(o, int): o = Rational(o, 1)
        return Rational(self.n * o.d + o.n * self.d, self.d * o.d)
    def __radd__(self, o): return self.__add__(o)
    def __sub__(self, o):
        if isinstance(o, int): o = Rational(o, 1)
        return Rational(self.n * o.d - o.n * self.d, self.d * o.d)
    def __rsub__(self, o): return Rational(o, 1).__sub__(self)
    def __mul__(self, o):
        if isinstance(o, int): o = Rational(o, 1)
        return Rational(self.n * o.n, self.d * o.d)
    def __rmul__(self, o): return self.__mul__(o)
    def __truediv__(self, o):
        if isinstance(o, int): o = Rational(o, 1)
        if o.n == 0: raise ZeroDivisionError("Division by zero")
        return Rational(self.n * o.d, self.d * o.n)
    def __rtruediv__(self, o): return Rational(o, 1).__truediv__(self)
    def __call__(self): return self.n / self.d
    def __getitem__(self, k):
        if k == "n": return self.n
        if k == "d": return self.d
    def __setitem__(self, k, v):
        if k == "n": self.n = int(v)
        elif k == "d": self.d = int(v)
        self.s()
    def __repr__(self): return f"{self.n}/{self.d}"

def tok(v):
    return Rational(v) if '/' in v else Rational(int(v), 1)

def e(v):
    t = v.split()
    if not t:
        raise ValueError("Порожній вираз")
    terms = []
    cur = tok(t[0])
    i = 1
    while i < len(t) - 1:
        op = t[i]
        x  = tok(t[i + 1])
        if op == '*':
            cur = cur * x
        elif op == '/':
            cur = cur / x
        elif op in ('+', '-'):
            terms.append(cur)
            cur = x if op == '+' else Rational(-x.n, x.d)
        else:
            raise ValueError(f"Невідомий оператор: {op}")
        i += 2
    terms.append(cur)
    r = Rational(0, 1)
    for val in terms:
        r = r + val
    return r

with open("C:\\Users\\User\\Desktop\\input01.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                res = e(line)
                print(f"Result: {res} ({res():.6f})")
            except Exception as m:
                print(f"Error: {m}")
            
