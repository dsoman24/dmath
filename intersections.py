# This is not a suitable algorithm, but it was a ~fun~ attempt. 
# Approximate points of intersections with magnitude
# upper and lower bound
# variable step size, minimum distance is point of intersection to certain level of precision determined by the step size.
# problems: this is basically just a "find the point with the shortest distance between two functions" prorgam, doest quite find the POI (works when you know the bounds though)
# next - find multiple values of intersection? different approach might be needed...
# 

from checkdp import cdp

def poi(lower, upper, func1, func2, step):
    """Point(s) of intersection of 2 functions (f1, f2) with a given step size. Returns tuple ((poi_x, poi_y), x, y_f1, y_f2)"""
    
    x = lower
    track_x = []
    track_magnitudes = []

    while x <= upper:
        try:
            s = abs(func1(x)-func2(x)) # distance between functions at the specific x value
        except ArithmeticError:
            pass # if /0 or other undefined values pass
        else:
            track_x.append(x)
            track_magnitudes.append(s)
            x += step # increments by step size
    
    min_magnitude = track_magnitudes[0]
    poi_index = 0
    
    for i in range(len(track_magnitudes)):
        if track_magnitudes[i] < min_magnitude:
            min_magnitude = track_magnitudes[i]
            poi_index = i
        
    x_poi = track_x[poi_index]
    y_poi = (func1(x_poi)+func2(x_poi))/2 # average y value in the approximation to get midpoint between two functions at the shortest distance
    #x_poi = round(x_poi, cdp(step))
    #y_poi = round(y_poi, cdp(step))
    
    return ((x_poi, y_poi)) 
    
# def f1(x):
#     y = 1/x
#     return y

# def f2(x):
#     y = x
#     return y

# p = poi(-2, 2, f1, f2, 0.000001)
# print(p)