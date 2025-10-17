import Params.Params as p
import math

def pixels_dist(x1,y1,x2,y2):
    return abs(x1-x2)

def find_dist(pixels, duo):
    return (p.PIXELS * p.d) / (2*p.tan_ALPHA*pixels - p.PIXELS*p.sigma_tan(duo))

def dist(points):
    dists = [0,0,0]
    for i in range(3):
        x1,y1=points[i]
        x2,x2=points[i+1]
        pixels=pixels_dist(x1,y1,x2,y2)
        dists[i] = find_dist(pixels,i) - p.camera_diff