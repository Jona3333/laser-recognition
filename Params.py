import math

class Params:
    PIXELS = 1920
    d = 0.06 # in cm
    ALPHA = math.radians(26.91)
    tan = math.tan(ALPHA)
    a = (PIXELS * d) / (2*tan)
    correction = 1
    A = a * correction