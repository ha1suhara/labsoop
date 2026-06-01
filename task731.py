from math import gcd


class RationalError(ZeroDivisionError):
    pass


class Rational:
    def __init__(self, n=0, d=1):
        if isinstance(n, Rational):
            self._n, self._d = n._n, n._d
            return
        if isinstance(n, str):
            n = n.strip()
            if '/' in n:
                a, b = n.split('/')
                n, d = int(a), int(b)
            else:
                n, d = int(n), 1
        n, d = int(n), int(d)
        if d == 0:
            raise RationalError("Знаменник = 0")
        if d < 0:
            n, d = -n, -d
        g = gcd(abs(n), d)
        self._n, self._d = n // g, d // g

    def __call__(self):
        return self._n / self._d

    def __getitem__(self, key):
        if key == 'n': return self._n
        if key == 'd': return self._d
        raise KeyError(key)

    def __setitem__(self, key, v):
        v = int(v)
        if key == 'n': self.__init__(v, self._d)
        elif key == 'd': self.__init__(self._n, v)
        else: raise KeyError(key)

    def __repr__(self):
        return str(self._n) if self._d == 1 else f"{self._n}/{self._d}"

    def _coerce(self, other):
        return other if isinstance(other, Rational) else Rational(other)

    def __add__(self, o):
        o = self._coerce(o)
        return Rational(self._n * o._d + o._n * self._d, self._d * o._d)
    def __radd__(self, o): return self.__add__(o)

    def __sub__(self, o):
        o = self._coerce(o)
        return Rational(self._n * o._d - o._n * self._d, self._d * o._d)
    def __rsub__(self, o): return Rational(o).__sub__(self)

    def __mul__(self, o):
        o = self._coerce(o)
        return Rational(self._n * o._n, self._d * o._d)
    def __rmul__(self, o): return self.__mul__(o)

    def __truediv__(self, o):
        o = self._coerce(o)
        return Rational(self._n * o._d, self._d * o._n)
    def __rtruediv__(self, o): return Rational(o).__truediv__(self)


if __name__ == '__main__':
    try:
        r = Rational(1, 0)
    except RationalError as e:
        print(f"RationalError: {e}")

    r = Rational("3/4")
    print(r)
