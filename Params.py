import math

class Params:
    PIXELS = 1920
    d = 0.06
    ALPHA = math.radians(26.91)
    tan = math.tan(ALPHA)
    A = (PIXELS * d) / (2*tan)