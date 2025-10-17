import Params as par
import math

'''
def pixels_dist(x1,y1,x2,y2):
    square = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
    return math.sqrt(square)
'''

def pixels_dist(x1, y1, x2, y2):
    return abs(x1-x2)

def dist(pixels):
    return par.Params.A * 1/pixels