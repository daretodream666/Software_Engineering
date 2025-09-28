from math import sqrt


def formula(a, b, c):
    s = float((a + b + c)) * 0.5
    return sqrt(s * (s - a) * (s - b) * (s - c))
